from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from config import (
    OLLAMA_BASE_URL, CHAT_MODEL, TEMPERATURE, SEED,
    MAX_TEXT_LENGTH, SUMMARY_BULLETS, QUIZ_QUESTIONS, QUIZ_OPTIONS,
)


def _llm():
    return ChatOllama(
        model=CHAT_MODEL,
        base_url=OLLAMA_BASE_URL,
        temperature=TEMPERATURE,
        seed=SEED,
    )


def summarize(text):
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a concise, factual summarizer."),
        ("human", f"Summarize in {SUMMARY_BULLETS} bullet points:\n\n{{text}}"),
    ])
    return (prompt | _llm()).invoke({"text": text[:MAX_TEXT_LENGTH]}).content


def make_quiz(text):
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You create clear multiple-choice quizzes."),
        ("human",
         f"Create {QUIZ_QUESTIONS} MCQs with {QUIZ_OPTIONS} options each "
         f"and mark the correct answer:\n\n{{text}}"),
    ])
    return (prompt | _llm()).invoke({"text": text[:MAX_TEXT_LENGTH]}).content
