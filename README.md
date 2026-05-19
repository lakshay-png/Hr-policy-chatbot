# HR Policy Chatbot using RAG + LangChain

AI-powered HR Policy Assistant built using LangChain, FAISS, Hugging Face, and Streamlit.

# Live Demo

[Hr-policy-chatbot](https://hr-policy-chatbot-nscuwappygnyb8ebcvmbkm7.streamlit.app/)

## RAG Workflow

This chatbot uses Retrieval-Augmented Generation (RAG) to retrieve relevant HR policy information from uploaded PDF documents before generating responses.

## Features

* Conversational HR policy chatbot
* Retrieval-Augmented Generation (RAG)
* PDF document ingestion
* Semantic search using FAISS
* Conversational memory support
* Streamlit interactive UI
* Hugging Face LLM integration

---

## Tech Stack

* Python
* LangChain
* Hugging Face
* FAISS
* Streamlit
* Sentence Transformers

---

## Project Architecture

1. Upload HR policy PDF
2. Extract text from documents
3. Split text into chunks
4. Generate embeddings
5. Store embeddings in FAISS vector database
6. Retrieve relevant chunks
7. Generate grounded response using LLM

---

## Installation

```bash
git clone https://github.com/lakshay-png/Hr-policy-chatbot.git

cd Hr-policy-chatbot

python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt
```

---

## Run the Application

```bash
streamlit run app.py
```

---

## Future Improvements

* Multi-PDF support
* Chat history persistence
* Authentication system
* Advanced prompt engineering
* Hybrid search retrieval

---

## Author

Lakshay Karwa
