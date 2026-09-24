import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "backend"))

import streamlit as st
import requests
from config import (
    BACKEND_URL, FRONTEND_TITLE, FRONTEND_ICON, ALLOWED_EXTENSIONS,
)

st.set_page_config(
    page_title=FRONTEND_TITLE,
    page_icon=FRONTEND_ICON,
    layout="wide",
)
st.title(f"{FRONTEND_ICON} {FRONTEND_TITLE}")

if "chat" not in st.session_state:
    st.session_state.chat = []
if "indexed" not in st.session_state:
    st.session_state.indexed = False

with st.sidebar:
    st.header("Upload a Document")
    file = st.file_uploader(
        "Choose a file",
        type=[e.lstrip(".") for e in ALLOWED_EXTENSIONS],
    )

    if file and st.button("Index Document", use_container_width=True):
        with st.spinner("Indexing..."):
            r = requests.post(
                f"{BACKEND_URL}/upload",
                files={"file": (file.name, file.getvalue())},
            )
        if r.status_code == 200:
            st.success(f"Indexed {r.json()['chunks']} chunks")
            st.session_state.indexed = True
        else:
            st.error(r.text)

    st.divider()

    if st.button("Summarize", use_container_width=True,
                 disabled=not st.session_state.indexed):
        with st.spinner("Summarizing..."):
            r = requests.get(f"{BACKEND_URL}/summarize")
        st.session_state.chat.append(("summary", r.json()["summary"]))

    if st.button("Generate Quiz", use_container_width=True,
                 disabled=not st.session_state.indexed):
        with st.spinner("Generating quiz..."):
            r = requests.get(f"{BACKEND_URL}/quiz")
        st.session_state.chat.append(("quiz", r.json()["quiz"]))

    if st.button("Reset", use_container_width=True):
        requests.post(f"{BACKEND_URL}/reset")
        st.session_state.chat = []
        st.session_state.indexed = False
        st.rerun()

for kind, content in st.session_state.chat:
    if kind in ("user", "assistant"):
        st.chat_message(kind).write(content)
    else:
        st.subheader(kind.capitalize())
        st.write(content)

question = st.chat_input(
    "Ask something about your document...",
    disabled=not st.session_state.indexed,
)
if question:
    st.session_state.chat.append(("user", question))
    with st.spinner("Thinking..."):
        r = requests.post(f"{BACKEND_URL}/ask", json={"question": question})
    st.session_state.chat.append(("assistant", r.json()["answer"]))
    st.rerun()
