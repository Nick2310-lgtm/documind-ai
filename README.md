# DocuMind AI

Local Ollama-powered document assistant. Upload a PDF/DOCX/TXT, 
ask questions, get summaries, and generate quizzes — all running 
fully offline with no API keys.

## Requirements

- Python 3.11 (tested on 3.11.9)
- Ollama installed: https://ollama.com/download
- 8 GB RAM minimum
- Windows / macOS / Linux

Python 3.12+ is not recommended — some dependencies 
(chromadb, pyarrow) lack prebuilt wheels for it.

## Setup

### 1. Pull Ollama models

```
ollama pull llama3.2:3b
ollama pull nomic-embed-text
```

### 2. Create virtual environment

```
python -m venv venv
```

Activate:

- macOS / Linux:
  ```
  source venv/bin/activate
  ```

- Windows PowerShell:
  ```
  .\venv\Scripts\Activate.ps1
  ```
  If scripts are blocked, run once:
  ```
  Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
  ```

- Windows CMD:
  ```
  venv\Scripts\activate.bat
  ```

### 3. Install dependencies

```
pip install -r requirements.txt
```

## Run

### Terminal 1 — Backend

```
cd backend
uvicorn main:app --reload
```

### Terminal 2 — Frontend

```
cd frontend
streamlit run app.py
```

Open **http://localhost:8501** in your browser.

## Endpoints

| Method | Path | Purpose |
|---|---|---|
| GET | /health | Liveness check |
| POST | /upload | Upload and index a document |
| POST | /ask | Answer a question |
| GET | /summarize | Summarize document |
| GET | /quiz | Generate quiz |
| POST | /reset | Clear session |

API docs available at http://localhost:8000/docs

## Configuration

All values are set in `.env`. Nothing is hardcoded in source.

Key variables:
- `OLLAMA_BASE_URL` — Ollama server URL
- `CHAT_MODEL` — LLM model tag
- `EMBED_MODEL` — embedding model tag
- `CHROMA_DIR` — vector DB directory
- `UPLOAD_DIR` — uploaded files directory
- `CHUNK_SIZE`, `CHUNK_OVERLAP`, `TOP_K` — RAG parameters

## Notes

- chromadb is pinned to `0.5.3` for compatibility with 
  `langchain-chroma==0.1.4`. Do not upgrade without testing.
- First query is slow (~15–45 s) while the LLM loads into RAM.
- Subsequent queries take ~5–15 s.

## License

Educational / mini-project use.
