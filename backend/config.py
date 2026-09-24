import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL")
CHAT_MODEL = os.getenv("CHAT_MODEL")
EMBED_MODEL = os.getenv("EMBED_MODEL")

CHROMA_DIR = str(BASE_DIR / os.getenv("CHROMA_DIR").lstrip("./"))
UPLOAD_DIR = str(BASE_DIR / os.getenv("UPLOAD_DIR").lstrip("./"))

CHUNK_SIZE = int(os.getenv("CHUNK_SIZE"))
CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP"))
TOP_K = int(os.getenv("TOP_K"))

TEMPERATURE = float(os.getenv("TEMPERATURE"))
SEED = int(os.getenv("SEED"))

BACKEND_HOST = os.getenv("BACKEND_HOST")
BACKEND_PORT = int(os.getenv("BACKEND_PORT"))
BACKEND_URL = os.getenv("BACKEND_URL")

FRONTEND_PORT = int(os.getenv("FRONTEND_PORT"))
FRONTEND_TITLE = os.getenv("FRONTEND_TITLE")
FRONTEND_ICON = os.getenv("FRONTEND_ICON")

MAX_TEXT_LENGTH = int(os.getenv("MAX_TEXT_LENGTH"))
SUMMARY_BULLETS = int(os.getenv("SUMMARY_BULLETS"))
QUIZ_QUESTIONS = int(os.getenv("QUIZ_QUESTIONS"))
QUIZ_OPTIONS = int(os.getenv("QUIZ_OPTIONS"))

ALLOWED_EXTENSIONS = [
    f".{e.strip().lower()}"
    for e in os.getenv("ALLOWED_EXTENSIONS").split(",")
]
