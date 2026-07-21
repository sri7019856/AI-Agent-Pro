from src.rag.embeddings import embeddings

texts = ["Hello", "How are you?"]

vectors = embeddings.embed_documents(texts)

print(len(vectors))
print(len(vectors[0]))
