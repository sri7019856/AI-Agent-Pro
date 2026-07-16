from src.rag.loader import load_pdf
from src.rag.splitter import split_documents
from src.rag.embeddings import embeddings

docs = load_pdf("Inflation tamed.pdf")
chunks = split_documents(docs)

print(len(chunks))

print("Embedding first chunk...")
vec = embeddings.embed_documents([chunks[0].page_content])

print(len(vec))
print("SUCCESS")