# DocuMind AI

Local Ollama-powered document assistant. Upload PDF/DOCX/TXT, ask 
questions, generate summaries and quizzes. Runs fully offline with 
no API keys.

## Requirements

- Python 3.11
- Ollama: https://ollama.com/download
- 8 GB RAM minimum

Python 3.12+ is not supported (dependency wheels unavailable).

## Setup

```
ollama pull llama3.2:3b
ollama pull nomic-embed-text

python -m venv venv
```

Activate (Windows PowerShell):
```
.\venv\Scripts\Activate.ps1
```

If blocked:
```
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

Install:
```
pip install -r requirements.txt
```

## Run

Terminal 1:
```
cd backend
uvicorn main:app --reload
```

Terminal 2:
```
cd frontend
streamlit run app.py
```

Open http://localhost:8501

## Endpoints

| Method | Path | Purpose |
|---|---|---|
| GET | /health | Liveness check |
| POST | /upload | Upload and index a document |
| POST | /ask | Answer a question |
| GET | /summarize | Summarize document |
| GET | /quiz | Generate quiz |
| POST | /reset | Clear session |

## Configuration

All values are set in `.env`. Nothing is hardcoded in source.

- `OLLAMA_BASE_URL`, `CHAT_MODEL`, `EMBED_MODEL`
- `CHROMA_DIR`, `UPLOAD_DIR`
- `CHUNK_SIZE`, `CHUNK_OVERLAP`, `TOP_K`
- `BACKEND_URL`, `FRONTEND_PORT`

Note: chromadb is pinned to 0.5.3 for compatibility with 
langchain-chroma==0.1.4.
