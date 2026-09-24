import os
import shutil
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from config import OLLAMA_BASE_URL, EMBED_MODEL, CHROMA_DIR


def _embeddings():
    return OllamaEmbeddings(model=EMBED_MODEL, base_url=OLLAMA_BASE_URL)


def build_store(chunks):
    if os.path.exists(CHROMA_DIR):
        shutil.rmtree(CHROMA_DIR)

    return Chroma.from_documents(
        documents=chunks,
        embedding=_embeddings(),
        persist_directory=CHROMA_DIR,
    )
