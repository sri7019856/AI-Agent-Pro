from src.rag.loader import load_pdf
from src.rag.splitter import split_documents

docs = load_pdf("student_application.pdf")

chunks = split_documents(docs)

print("Chunks:", len(chunks))

for i, chunk in enumerate(chunks):
    print("="*60)
    print("Chunk", i)
    print("Length:", len(chunk.page_content))
    print(chunk.page_content)