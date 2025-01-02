# OpenAI Document Q&A System

## Overview

This project implements a backend service using **FastAPI** to handle document ingestion, question answering (Q&A), and document selection. It stores documents and their embeddings in a **PostgreSQL** database and utilizes the **OpenAI API** to generate answers based on the context of relevant documents. The system is designed to help users upload documents, query them for specific information, and select relevant documents for further processing.

## Features

- **Document Ingestion**: Upload and store documents along with their embeddings in a PostgreSQL database.
- **Q&A**: Given a user query, retrieve relevant documents and use OpenAI to generate an answer based on those documents.
- **Document Selection**: Select specific documents by IDs for further processing.

## Technologies Used

- **FastAPI**: A modern, fast (high-performance) web framework for building APIs with Python 3.7+.
- **PostgreSQL**: A powerful, open-source relational database system used for storing documents and their embeddings.
- **SQLAlchemy (Async)**: A SQL toolkit and Object-Relational Mapping (ORM) library for Python that supports asynchronous operations.
- **OpenAI API**: For generating responses using OpenAI's models based on document context.

## Setup Instructions

### Prerequisites

- **Python 3.8+**
- **PostgreSQL**: Ensure that PostgreSQL is installed and running on your local machine or use a cloud instance.
- **API Key for OpenAI**: You will need an OpenAI API key to use the OpenAI models.

### 1. Clone the Repository

Clone the project from GitHub:

```bash
git clone https://github.com/priya2710/OpenAIModel.git
cd OpenAIModel
```

### 2. Set Up a Virtual Environment

Create and activate a virtual environment:

```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies

Install the required Python dependencies:

```bash
pip install -r requirements.txt
```

### 4. Set Up PostgreSQL Database

1. Install PostgreSQL and create a new database (e.g., `python-backend`).
2. Update your `DATABASE_URL` in `database.py` with your PostgreSQL connection string. For example:

```python
DATABASE_URL = "postgresql+asyncpg://postgres:password@localhost/python-backend"
```

### 5. Set Up OpenAI API Key

1. Obtain an OpenAI API key by signing up at [OpenAI API](https://platform.openai.com/account/api-keys).
2. Set the API key in the `utils.py` file:

```python
openai.api_key = 'your-api-key-here'
```

Alternatively, you can set the environment variable `OPENAI_API_KEY` for added security.

### 6. Run the Application

Once all dependencies are installed and configurations are set, run the FastAPI application:

```bash
uvicorn main:app --reload
```

Your API will be available at `http://127.0.0.1:8000`.

### 7. Test the API

You can test the API endpoints using tools like Postman or cURL.
(For better understanding, attached Postman collection in this repository)

### API Endpoints:

- **POST /api/ingestion/ingest**: Upload documents along with embeddings.
- **POST /api/qna**: Ask a question and get an answer based on document context.
- **GET /api/selection/select**: Select documents by their IDs.

### Example of a POST Request (Q&A)

Example of how to ask a question using Postman or cURL:

**URL**: `http://127.0.0.1:8000/api/qna`

**Request Body**:
```json
{
  "query": "What is the capital of France?"
}
```

**Response**:
```json
{
  "query": "What is the capital of France?",
  "answer": "Paris is the capital of France.",
  "relevant_documents": [
    {
      "filename": "document1.txt",
      "content": "Some document content..."
    },
    {
      "filename": "document2.txt",
      "content": "Another document content..."
    }
  ]
}
```

## How It Works

### 1. Document Ingestion

- Use the `/api/ingestion` endpoint to upload documents. The system stores both the document content and its corresponding embeddings in the PostgreSQL database. Embeddings are generated using a sentence-transformer model.

### 2. Q&A Workflow

- Use the `/api/qna` endpoint to ask questions. The system:
  1. Retrieves relevant documents based on embedding similarity between the query and stored documents.
  2. Uses OpenAI's GPT model to generate an answer by considering the context from the relevant documents.

### 3. Document Selection

- Use the `/api/selection/select` endpoint to select specific documents by their IDs. The system retrieves and returns the documents with the given IDs for further analysis or processing.

## Troubleshooting

- **Database Connection Issues**: Ensure that the PostgreSQL server is running and the connection string in `database.py` is correct.
- **OpenAI API Key**: Make sure the correct API key is set in the `utils.py` file or as an environment variable.
- **Missing Dependencies**: Run `pip install -r requirements.txt` to install any missing libraries.
- **Document Ingestion Errors**: Ensure that the document files being uploaded are valid and the embeddings are generated correctly.

## Contributing

Feel free to contribute to the project by forking the repository, making improvements, and submitting pull requests. Ensure that you follow the existing code structure and conventions. If you encounter any issues, feel free to open an issue in the GitHub repository.
