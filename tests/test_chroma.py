from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings

embeddings = OllamaEmbeddings(model="nomic-embed-text")

db = Chroma(
    collection_name="test_collection",
    persist_directory="test_db",
    embedding_function=embeddings,
)

print("Embedding manually...")

vec = embeddings.embed_documents(["Hello world"])

print("Embedding done")

print(vec[0][:5])