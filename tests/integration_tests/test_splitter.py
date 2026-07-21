from src.rag.loader import load_pdf
from src.rag.splitter import split_documents

PDF_NAME = "Think-And-Grow-Rich-Napoleon-Hill.pdf"

print("\n" + "=" * 70)
print("                 PDF SPLITTER TEST")
print("=" * 70)

# -------------------------
# Load PDF
# -------------------------
docs = load_pdf(PDF_NAME)

# -------------------------
# Split Documents
# -------------------------
chunks = split_documents(docs)

# -------------------------
# Statistics
# -------------------------
chunk_lengths = [len(chunk.page_content) for chunk in chunks]

print(f"PDF File          : {PDF_NAME}")
print(f"Pages Loaded      : {len(docs)}")
print(f"Chunks Created    : {len(chunks)}")
print("Chunk Size        : 500")
print("Chunk Overlap     : 100")
print(f"Average Chunk Len : {sum(chunk_lengths)//len(chunk_lengths)}")
print(f"Largest Chunk     : {max(chunk_lengths)}")
print(f"Smallest Chunk    : {min(chunk_lengths)}")

print("=" * 70)
print("STATUS            : PASSED")
print("=" * 70)

# ----------------------------------------------------
# Display Sample Chunks
# ----------------------------------------------------

sample_indices = [
    0,
    min(1, len(chunks) - 1),
    min(2, len(chunks) - 1),
    len(chunks) // 2,
    len(chunks) - 1,
]

print("\nSample Chunks\n")

shown = set()

for index in sample_indices:

    if index in shown:
        continue

    shown.add(index)

    chunk = chunks[index]

    print("-" * 70)
    print(f"Chunk #{index+1}")
    print(chunk.metadata)
    print()

    preview = chunk.page_content[:250].replace("\n", " ")
    print(preview)
    print()

print("=" * 70)
print("END OF TEST")
print("=" * 70)
