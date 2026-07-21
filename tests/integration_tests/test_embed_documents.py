from src.rag.embeddings import embeddings

docs = ["Python is a programming language.", "Java is also a programming language."]

print("Embedding documents...")

vectors = embeddings.embed_documents(docs)

print("Done!")

print(len(vectors))
print(len(vectors[0]))
