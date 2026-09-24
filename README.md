# DocuMind AI

Local Ollama-powered document assistant.

## Requirements

- Python 3.10 or 3.11
- Ollama installed: https://ollama.com/download
- 8 GB RAM minimum

## Setup

```bash
ollama pull llama3.2:3b
ollama pull nomic-embed-text

python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Windows activation:

```bash
venv\Scripts\activate
```

## Run

Terminal 1:

```bash
cd backend
uvicorn main:app --reload
```

Terminal 2:

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
