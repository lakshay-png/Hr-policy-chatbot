import os
import streamlit as st
from dotenv import load_dotenv

from app.backend.pdf_loader import load_pdf
from app.backend.text_splitter import split_documents
from app.backend.vector_store import (
    create_vectorstore,
    save_vectorstore,
    load_vectorstore
)

from app.backend.chatbot import create_chatbot
from app.backend.auth import login
from app.frontend.ui import load_css

load_dotenv()

st.set_page_config(
    page_title="HR Policy Chatbot",
    page_icon="🤖",
    layout="wide"
)

load_css()

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    login()
    st.stop()

st.title("🤖 Company Policy & HR Chatbot")

with st.sidebar:

    st.header("📄 Upload HR PDFs")

    uploaded_files = st.file_uploader(
        "Upload PDF files",
        type=["pdf"],
        accept_multiple_files=True
    )

    if st.button("Process PDFs"):

        all_documents = []

        with st.spinner("Processing PDFs..."):

            for file in uploaded_files:

                file_path = os.path.join("uploads", file.name)

                with open(file_path, "wb") as f:
                    f.write(file.getbuffer())

                documents = load_pdf(file_path)
                all_documents.extend(documents)

            chunks = split_documents(all_documents)

            vectorstore = create_vectorstore(chunks)

            save_vectorstore(vectorstore)

            st.success("PDFs processed successfully!")

    if st.button("Clear Chat"):
        st.session_state.messages = []

    if st.button("Export Chat"):

        chat_text = ""

        for msg in st.session_state.messages:
            chat_text += f"{msg['role']}: {msg['content']}\n"

        st.download_button(
            label="Download Chat",
            data=chat_text,
            file_name="chat_history.txt"
        )

suggested_questions = [
    "How many sick leaves do I get?",
    "Can leaves be carried forward?",
    "What is the work from home policy?",
    "Explain attendance rules"
]

st.sidebar.subheader("💡 Suggested Questions")

for question in suggested_questions:
    if st.sidebar.button(question):
        st.session_state.user_question = question

if "messages" not in st.session_state:
    st.session_state.messages = []

user_question = st.chat_input("Ask your HR policy question...")

if "user_question" in st.session_state:
    user_question = st.session_state.user_question

if user_question:

    st.session_state.messages.append({
        "role": "user",
        "content": user_question
    })

    for msg in st.session_state.messages:

        if msg["role"] == "user":
            with st.chat_message("user"):
                st.markdown(msg["content"])

        else:
            with st.chat_message("assistant"):
                st.markdown(msg["content"])

    with st.spinner("Thinking..."):

        db = load_vectorstore()

        chatbot = create_chatbot(db)

        response = chatbot({"question": user_question})

        answer = response["answer"]

        sources = response["source_documents"]

        source_text = ""

        for source in sources:
            source_text += f"\n\n📌 Source: {source.metadata}"

        final_answer = answer + source_text

        st.session_state.messages.append({
            "role": "assistant",
            "content": final_answer
        })

        with st.chat_message("assistant"):
            st.markdown(final_answer)