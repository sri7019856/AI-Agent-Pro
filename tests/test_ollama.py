from src.llm import llm

print("=" * 50)
print("Testing Ollama")
print("=" * 50)

response = llm.invoke("Who are you?")

print(response.content)