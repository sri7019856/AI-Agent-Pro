from src.rag.embeddings import embeddings

print("Testing Ollama embeddings...")

vector = embeddings.embed_query("Hello from my AI Agent!")

print("Embedding dimension:", len(vector))
print("First 5 values:", vector[:5])

print("SUCCESS")