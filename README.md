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

### 1. Clone

```bash
git clone https://github.com/YOUR_USERNAME/documind-ai.git
cd documind-ai
```

### 2. Pull Ollama models

```bash
ollama pull llama3.2:3b
ollama pull nomic-embed-text
```

### 3. Create virtual environment

```bash
python -m venv venv
```

Activate (Windows PowerShell):

```powershell
.\venv\Scripts\Activate.ps1
```

If blocked:

```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

### 4. Create `.env`

Create a file named `.env` in the project root with the following content:

```
OLLAMA_BASE_URL=http://localhost:11434
CHAT_MODEL=llama3.2:3b
EMBED_MODEL=nomic-embed-text:latest
CHROMA_DIR=./chroma_db
UPLOAD_DIR=./uploads
CHUNK_SIZE=1500
CHUNK_OVERLAP=200
TOP_K=4
TEMPERATURE=0.0
SEED=42
BACKEND_HOST=0.0.0.0
BACKEND_PORT=8000
BACKEND_URL=http://localhost:8000
FRONTEND_PORT=8501
FRONTEND_TITLE=DocuMind AI
FRONTEND_ICON=📚
MAX_TEXT_LENGTH=12000
SUMMARY_BULLETS=8
QUIZ_QUESTIONS=5
QUIZ_OPTIONS=4
ALLOWED_EXTENSIONS=pdf,docx,txt
```

The file must be named exactly `.env` — no `.txt` extension.

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

## Run

### Terminal 1 (from project root) — Backend

```bash
cd backend
uvicorn main:app --reload
```

### Terminal 2 (from project root) — Frontend

```bash
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

Note: chromadb is pinned to `0.5.3` for compatibility with 
`langchain-chroma==0.1.4`.
