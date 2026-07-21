from src.rag.loader import load_pdf

PDF_NAME = "Think-And-Grow-Rich-Napoleon-Hill.pdf"

print("\n" + "=" * 70)
print("                    PDF LOADER TEST")
print("=" * 70)

# -------------------------------------------------
# Load PDF
# -------------------------------------------------

docs = load_pdf(PDF_NAME)

# -------------------------------------------------
# Statistics
# -------------------------------------------------

print(f"PDF File          : {PDF_NAME}")
print(f"Pages Loaded      : {len(docs)}")

print("=" * 70)
print("STATUS            : PASSED")
print("=" * 70)

# -------------------------------------------------
# Sample Pages
# -------------------------------------------------

sample_indices = [0, min(1, len(docs) - 1), len(docs) // 2, len(docs) - 1]

shown = set()

print("\nSample Pages\n")

for index in sample_indices:

    if index in shown:
        continue

    shown.add(index)

    page = docs[index]

    print("-" * 70)
    print(f"Page #{index + 1}")
    print(page.metadata)
    print()

    preview = page.page_content[:300].replace("\n", " ")
    print(preview)
    print()

print("=" * 70)
print("END OF TEST")
print("=" * 70)
