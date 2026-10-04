# 📄 Chat With Your PDF API

A FastAPI-based project that allows users to upload PDF documents, extract their text, and interact with the document using an AI/LLM. The project is designed as a **Chat With Your PDF API**, where users can upload a PDF and ask questions about its content.

## 🚀 Features

* 📤 Upload PDF documents
* 📑 Extract text from PDF files
* 🤖 Generate AI-based responses from PDF content
* 💬 Chat with uploaded PDF documents
* 🔑 Support for Google Gemini API
* 🗂️ Store uploaded document information using unique UUIDs
* ⚡ Fast and lightweight REST API using FastAPI
* 📚 Interactive API documentation with Swagger UI
* 🔍 Query PDF content through API endpoints

## 🛠️ Technologies Used

* **Python 3.11**
* **FastAPI**
* **Uvicorn**
* **Google Gemini API**
* **PyPDF**
* **Pydantic**
* **python-multipart**
* **UUID**
* **dotenv / Environment Variables**

## 📁 Project Structure

```text
project code/
│
├── main.py
├── README.md
├── requirements.txt
│
└── src/
    │
    ├── data_store.py
    │
    ├── routers/
    │   └── data_handler.py
    │
    └── utils/
        ├── pdf_processor.py
        └── llm_client.py
```

## 📌 File Description

### `main.py`

The main entry point of the FastAPI application.

It:

* Creates the FastAPI application
* Includes the application router
* Defines the API prefix
* Provides the main application configuration

Example:

```python
from fastapi import FastAPI
from src.routers import data_handler

app = FastAPI(
    title="CAG Project API - Chat With Your PDF",
    description="API for uploading PDFs, querying content via LLM, and managing data.",
    version="0.1.0",
)

app.include_router(
    data_handler.router,
    prefix="/api/v1",
    tags=["Data Handling and Chat With PDF"],
)
```

### `data_handler.py`

Contains the API routes related to:

* PDF uploading
* PDF processing
* Document handling
* Asking questions about uploaded documents

### `pdf_processor.py`

Contains utility functions for processing PDF files and extracting their text.

### `llm_client.py`

Handles communication with the LLM/API and generates responses based on the user's query and document content.

### `data_store.py`

Provides a temporary storage mechanism for uploaded document information during application execution.

### `requirements.txt`

Contains the Python packages required to run the project.

## ⚙️ Installation

### 1. Clone or download the project

Open your terminal and navigate to the project directory.

```powershell
cd "D:\object_oriented_programming1.py\hope-to-skills.py\project code"
```

### 2. Create a virtual environment

If you don't already have one:

```powershell
python -m venv .venv
```

### 3. Activate the virtual environment

On Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

You should see:

```text
(.venv)
```

at the beginning of your terminal.

### 4. Install dependencies

```powershell
pip install -r requirements.txt
```

If you don't have a `requirements.txt` file yet, you can install the main packages with:

```powershell
pip install fastapi uvicorn python-multipart pypdf google-genai python-dotenv
```

## 🔐 Environment Variables

Create a `.env` file in the project root:

```text
GEMINI_API_KEY=your_api_key_here
```

Replace:

```text
your_api_key_here
```

with your actual Google Gemini API key.

### ⚠️ Important

Do not upload your `.env` file or API key to GitHub.

Add this to your `.gitignore`:

```text
.env
.venv/
__pycache__/
*.pyc
```

## ▶️ Running the Application

Make sure your virtual environment is activated.

Run:

```powershell
uvicorn main:app --reload --port 8001
```

If everything is working correctly, you should see:

```text
Uvicorn running on http://127.0.0.1:8001
```

## 📚 API Documentation

FastAPI automatically provides interactive API documentation.

### Swagger UI

Open:

```text
http://127.0.0.1:8001/docs
```

### ReDoc

Open:

```text
http://127.0.0.1:8001/redoc
```

Swagger UI allows you to test your API directly from your browser.

## 🔄 How the Project Works

The basic workflow is:

```text
User
  │
  ▼
Upload PDF
  │
  ▼
FastAPI
  │
  ▼
PDF Processor
  │
  ▼
Extract Text
  │
  ▼
Store Document
  │
  ▼
User Asks Question
  │
  ▼
LLM Client
  │
  ▼
Google Gemini API
  │
  ▼
AI Response
  │
  ▼
User
```

## 🆔 UUID for Documents

Each uploaded document can be assigned a unique UUID.

Example:

```python
import uuid

pdf_id = str(uuid.uuid4())
```

A generated UUID may look like:

```text
7c9e6679-7425-40de-944b-e07fc1f90ae7
```

Using UUIDs helps uniquely identify uploaded documents.

## 📤 Example Upload

A PDF can be uploaded through the API using the FastAPI Swagger interface.

Example request:

```text
POST /api/v1/upload
```

The uploaded file can then be processed and associated with a unique document ID.

## 💬 Chat With PDF

After a PDF has been uploaded, the application can use its extracted content to process user questions.

Example:

```text
User:
What is the main purpose of this document?

AI:
The main purpose of the document is ...
```

## 🧪 Testing

You can test the API using:

* FastAPI Swagger UI
* Postman
* Thunder Client
* Python requests
* Any REST API client

Swagger is available at:

```text
http://127.0.0.1:8001/docs
```

## 🐛 Troubleshooting

### FastAPI import error

Make sure your FastAPI imports use the correct capitalization:

```python
from fastapi import APIRouter, UploadFile, File, HTTPException, Query
```

Use:

```python
File
```

not:

```python
file
```

### Router import error

Make sure `data_handler.py` contains:

```python
router = APIRouter()
```

and `main.py` includes:

```python
app.include_router(
    data_handler.router,
    prefix="/api/v1",
)
```

### LLM function import error

Make sure the function name in `llm_client.py` exactly matches the function being imported in `data_handler.py`.

For example:

```python
from src.utils.llm_client import get_llm_response
```

Make sure `llm_client.py` actually contains:

```python
def get_llm_response(...):
    ...
```

Remember that Python is case-sensitive and spelling must match exactly.

## 🔒 Security

* Keep API keys inside `.env`
* Never commit API keys to GitHub
* Add `.env` to `.gitignore`
* Validate uploaded files
* Restrict uploads to supported file types such as PDF
* Handle API errors appropriately

## 🎯 Future Improvements

Possible future improvements include:

* Persistent database storage
* Multiple PDF support
* Conversation history
* Authentication and authorization
* Vector database integration
* Embeddings and semantic search
* RAG-based document retrieval
* Better document chunking
* User-specific document management
* Deployment to a cloud platform

## 👨‍💻 Author

**Muhammad Naeem**

Computer Science | AI/ML Enthusiast

GitHub: `github.com/naeem847`

## 📄 License

This project is currently developed for educational and learning purposes.
