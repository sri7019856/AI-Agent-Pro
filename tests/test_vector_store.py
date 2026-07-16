from src.rag.loader import load_pdf
from src.rag.splitter import split_documents
from src.rag.vector_store import create_vector_store

PDF_NAME = "Inflation tamed.pdf"

print("=" * 70)
print("                VECTOR STORE TEST")
print("=" * 70)
# Step 1
docs = load_pdf(PDF_NAME)
print(f"✓ PDF Loaded      : {len(docs)} pages")

# Step 2
chunks = split_documents(docs)
print(f"✓ Chunks Created  : {len(chunks)}")

# Step 3
print("Creating Chroma database...")
vectorstore = create_vector_store(chunks)
print("✓ Chroma Database Created")

# Step 4
count = vectorstore.index.ntotal

print(f"Vectors stored: {count}")

assert count == len(chunks)

print(f"✓ Vectors Stored  : {count}")

assert count == len(chunks), "Mismatch between chunks and stored vectors!"

print("=" * 70)
print("STATUS : PASSED")
print("=" * 70)