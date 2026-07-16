from langchain_chroma import Chroma
from src.rag.embeddings import embeddings


def create_vector_store(chunks):

    db = Chroma(
        persist_directory="chroma_db",
        embedding_function=embeddings,
    )

    db.add_documents(chunks)

    return db


def load_vector_store():

    return Chroma(
        persist_directory="chroma_db",
        embedding_function=embeddings,
    )