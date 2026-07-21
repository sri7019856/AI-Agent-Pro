from src.rag.vector_store import load_vector_store

db = load_vector_store()

retriever = db.as_retriever(search_kwargs={"k": 3})
