from src.rag.chain import ask_pdf

question = input("Ask a question: ")

answer = ask_pdf(question)

print("\nAnswer:\n")
print(answer)