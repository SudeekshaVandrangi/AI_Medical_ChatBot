import streamlit as st
from src.helper import download_hugginface_embedding
from langchain_pinecone import PineconeVectorStore
import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from src.prompt import system_prompt
import os

# Load environment variables
load_dotenv()
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY
os.environ["GEMINI_API_KEY"] = GEMINI_API_KEY

# Download embeddings
embeddings = download_hugginface_embedding()

# Load the existing index from Pinecone
index_name = "medicalbot"
docsearch = PineconeVectorStore.from_existing_index(index_name=index_name, embedding=embeddings)
retriever = docsearch.as_retriever(search_type="similarity", search_kwargs={"k": 10})

# Initialize the LLM
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", google_api_key=GEMINI_API_KEY)
system_prompt = (
    "You are a knowledgeable assistant tasked with answering questions based on the full provided context. "
    "Analyze all the information before generating a response. "
    "Do not rely on individual sentences in isolation—synthesize information across the entire context. "
    "If the answer cannot be determined from the context, respond with 'I don't know.' "
    "Your answer should be clear, accurate.\n\n{context}"
)

prompt = ChatPromptTemplate.from_messages([("system", system_prompt), ("human", "{input}")])
question_answer_chain = create_stuff_documents_chain(llm=llm, prompt=prompt)
rag_chain = create_retrieval_chain(retriever, question_answer_chain)

# Streamlit frontend
def main():
    st.set_page_config(page_title="Medical Bot", page_icon="💬")

    # Sidebar with bot and developer info
    with st.sidebar:
        st.image("https://cdn-icons-png.flaticon.com/512/3774/3774299.png", width=100)
        st.title("🤖 Medical Bot Info")

        st.markdown("""
        **Model Description:**  
        This assistant uses advanced RAG techniques combining **gemini-2.0-flash** and **Pinecone** vector search.  
        It provides reliable, grounded answers sourced from *The Gale Encyclopedia of Medicine (3rd Edition)*.

        **Developer:**  
        **Mohammed Hamza Khalifa**  
        AI Engineer | Passionate about machine learning, NLP, and real-world AI solutions.

        [🔗 Connect on LinkedIn](https://www.linkedin.com/in/mohammed-hamza-4184b2251/)

        ---

        © 2025 Mohammed Khalifa
        """)

    # Custom CSS styling
    st.markdown("""
        <style>
        .chat-container {
            width: 100%;
            max-width: 700px;
            margin: 0 auto;
            background-color: #131722;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }
        .chat-message {
            margin-bottom: 12px;
            padding: 10px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        .chat-message.user {
            background-color: #0a5e2a;
            text-align: right;
            flex-direction: row-reverse;
            color: #e8ebf1;
        }
        .chat-message.bot {
            background-color: #e1f7d5;
            text-align: left;
            flex-direction: row;
            color: #131722;
        }
        .chat-avatar {
            width: 40px;
            height: 40px;
            border-radius: 50%;
            margin-right: 10px;
        }
        .header {
            text-align: center;
            padding: 10px;
            background-color: #1E90FF;
            color: white;
            border-radius: 8px;
        }
        .stTextInput>div>div>input {
            font-size: 16px;
            background-color: #1d2330;
            color: #e8ebf1;
        }
        body {
            color: #e8ebf1;
            background-color: #131722;
        }
        </style>
    """, unsafe_allow_html=True)

    # Avatars
    doctor_avatar = "https://img.poki-cdn.com/cdn-cgi/image/quality=78,width=628,height=628,fit=cover,f=auto/92516ad387af67f26d5a217c5381a41f.png"
    user_avatar = "https://cdn-icons-png.freepik.com/512/6596/6596121.png"

    st.markdown("<h2 class='header'>Medical Bot</h2>", unsafe_allow_html=True)
    st.write("Ask me anything related to medical information.")

    # Initialize history
    if "history" not in st.session_state:
        st.session_state.history = []

    # Input from user
    user_input = st.text_input("Your question:", key="user_input")

    # Handle send
    if st.button("Send"):
        if user_input:
            st.session_state.history.append({"role": "user", "message": user_input})
            response = rag_chain.invoke({"input": user_input})
            bot_answer = response["answer"]
            st.session_state.history.append({"role": "bot", "message": bot_answer})

    # Clear history
    if st.button("🧹 Clear Chat"):
        st.session_state.history = []
        st.rerun()

    # Display chat history
    with st.container():
        for chat in st.session_state.history:
            if chat["role"] == "user":
                st.markdown(f'''
                    <div class="chat-message user">
                        <img class="chat-avatar" src="{user_avatar}" alt="User Avatar"/>
                        <div>{chat["message"]}</div>
                    </div>
                ''', unsafe_allow_html=True)
            else:
                st.markdown(f'''
                    <div class="chat-message bot">
                        <img class="chat-avatar" src="{doctor_avatar}" alt="Doctor Avatar"/>
                        <div>{chat["message"]}</div>
                    </div>
                ''', unsafe_allow_html=True)

    # Auto scroll
    st.markdown('<script>window.scrollTo(0, document.body.scrollHeight);</script>', unsafe_allow_html=True)


if __name__ == "__main__":
    main()
