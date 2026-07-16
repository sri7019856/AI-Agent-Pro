from pathlib import Path

from pypdf import PdfReader
from langchain_core.documents import Document


DOCUMENTS_DIR = Path("documents")


def load_pdf(filename: str):

    path = DOCUMENTS_DIR / filename

    if not path.exists():
        raise FileNotFoundError(
            f"{path} does not exist. Put your PDF inside the 'documents' folder."                      
        )

    reader = PdfReader(path)

    documents = []

    for page_number, page in enumerate(reader.pages):

        text = page.extract_text()

        if text:

            documents.append(
                Document(
                    page_content=text,
                    metadata={
                        "source": filename,
                        "page": page_number + 1,
                    },
                )
            )

    return documents