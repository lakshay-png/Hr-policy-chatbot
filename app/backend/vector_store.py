from langchain_community.vectorstores import FAISS
from app.backend.embeddings import get_embeddings

def create_vectorstore(chunks):
    embeddings = get_embeddings()

# FAISS vector database initialized for semantic similarity search
    vectorstore = FAISS.from_documents(
        documents=chunks,
        embedding=embeddings
    )

    return vectorstore


def save_vectorstore(vectorstore):
    vectorstore.save_local("vectorstore/db_faiss")


def load_vectorstore():
    embeddings = get_embeddings()

    db = FAISS.load_local(
        "vectorstore/db_faiss",
        embeddings,
        allow_dangerous_deserialization=True
    )

    return db