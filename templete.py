import os
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="[%(asctime)s]: %(message)s:")


list_of_files = [
     "src/__init__.py",
     "src/helper.py",
     "src/prompt.py",
     ".env",
     "setup.py",
     "app.py",
     "research/trial.ipynb",
     "test.py"
]

for filepath in list_of_files:
     filepath = Path(filepath)
     filedir, filename = os.path.split(filepath)
     if filedir != "":
          os.makedirs(filedir, exist_ok=True)
          logging.info(f"Creating Directory {filedir} for the file name {filename}")
          
     if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0 ):
          with open(file=filepath, mode="w") as f:
               pass
               logging.info(f"Creating empty file: {filepath}")
               
     else:
          logging.info(f"{filepath} is already exists")