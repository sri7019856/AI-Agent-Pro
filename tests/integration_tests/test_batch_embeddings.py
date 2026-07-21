from src.rag.loader import load_pdf
from src.rag.splitter import split_documents
from src.rag.embeddings import embeddings

docs = load_pdf("Inflation tamed.pdf")
chunks = split_documents(docs)

texts = [chunk.page_content for chunk in chunks[:10]]

print("Embedding 10 documents...")

vectors = embeddings.embed_documents(texts)

print(f"Created {len(vectors)} embeddings")
print("SUCCESS")
