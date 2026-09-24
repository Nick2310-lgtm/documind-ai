import os
import shutil
from fastapi import FastAPI, UploadFile, File, HTTPException
from pydantic import BaseModel

from ingestion import load_and_split
from vectorstore import build_store
from rag_chain import build_qa_chain
from generators import summarize, make_quiz
from config import UPLOAD_DIR

app = FastAPI()
STATE = {}


class Query(BaseModel):
    question: str


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    os.makedirs(UPLOAD_DIR, exist_ok=True)
    path = os.path.join(UPLOAD_DIR, file.filename)

    with open(path, "wb") as f:
        shutil.copyfileobj(file.file, f)

    try:
        chunks = load_and_split(path)
        if not chunks:
            raise HTTPException(400, "No text extracted")

        STATE["chain"] = build_qa_chain(build_store(chunks))
        STATE["full_text"] = "\n".join(c.page_content for c in chunks)

        return {"status": "indexed", "chunks": len(chunks)}
    except Exception as e:
        raise HTTPException(500, f"Ingestion failed: {e}")


@app.post("/ask")
def ask(q: Query):
    if "chain" not in STATE:
        raise HTTPException(400, "Upload a document first")
    return {"answer": STATE["chain"]({"question": q.question})["answer"]}


@app.get("/summarize")
def summarize_doc():
    if "full_text" not in STATE:
        raise HTTPException(400, "Upload a document first")
    return {"summary": summarize(STATE["full_text"])}


@app.get("/quiz")
def quiz():
    if "full_text" not in STATE:
        raise HTTPException(400, "Upload a document first")
    return {"quiz": make_quiz(STATE["full_text"])}


@app.post("/reset")
def reset():
    STATE.clear()
    return {"status": "reset"}
