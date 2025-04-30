# AI Medical ChatBot

A sophisticated medical chatbot powered by advanced AI technologies, designed to provide accurate and helpful medical information based on a comprehensive medical knowledge base.

## 🚀 Features

- **Intelligent Medical Responses**: Utilizes Google's Gemini 2.0 Flash model for generating accurate medical information
- **Vector Search**: Implements Pinecone vector store for efficient semantic search across medical documents
- **Modern UI**: Built with Streamlit for a clean and intuitive user interface
- **Secure**: Environment variable management for API keys and sensitive data
- **Scalable**: Modular architecture with separate components for embeddings, prompts, and data processing

## 🛠️ Technologies

- **Language Model**: Google Gemini 2.0 Flash
- **Vector Database**: Pinecone
- **Embeddings**: Sentence Transformers
- **Framework**: LangChain
- **UI**: Streamlit
- **PDF Processing**: PyPDF

## 📋 Prerequisites

- Python 3.8+
- Pinecone API key
- Google Gemini API key

## 🚀 Usage

### Local Development

1. Start the application:
```bash
streamlit run app.py
```

2. Open your browser and navigate to the provided local URL (typically http://localhost:8501)

3. Enter your medical questions in the chat interface

### Streamlit Cloud Deployment

1. Create a [Streamlit Cloud](https://streamlit.io/cloud) account if you haven't already

2. Connect your GitHub repository to Streamlit Cloud:
   - Go to https://share.streamlit.io/
   - Click "New app"
   - Select your repository, branch, and main file path (app.py)

3. Configure your secrets in Streamlit Cloud:
   - In your app settings, go to "Secrets"
   - Add your environment variables:
     ```toml
     PINECONE_API_KEY = "your_pinecone_api_key"
     GEMINI_API_KEY = "your_gemini_api_key"
     ```

4. Deploy your app:
   - Click "Deploy"
   - Streamlit Cloud will automatically build and deploy your application

## 📁 Project Structure

```
AI-Medical-ChatBot/
├── app.py              # Main application file
├── src/               # Source code directory
├── Data/              # Medical knowledge base
├── research/          # Research and documentation
├── requirements.txt   # Project dependencies
├── .streamlit/       # Streamlit configuration
│   └── config.toml   # Streamlit settings
└── .env              # Environment variables
```


## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Disclaimer

This chatbot is designed for informational purposes only and should not be used as a substitute for professional medical advice, diagnosis, or treatment. Always seek the advice of your physician or other qualified health provider with any questions you may have regarding a medical condition.
