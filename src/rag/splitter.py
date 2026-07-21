from langchain_core.documents import Document


def split_documents(documents, chunk_size=500, chunk_overlap=100):
    """
    Split Document objects into overlapping chunks.
    """

    chunks = []

    step = chunk_size - chunk_overlap

    for doc in documents:

        text = doc.page_content

        for i in range(0, len(text), step):

            chunk_text = text[i : i + chunk_size]

            chunks.append(
                Document(page_content=chunk_text, metadata=doc.metadata.copy())
            )

    return chunks
