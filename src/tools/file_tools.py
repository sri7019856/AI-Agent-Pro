from langchain_core.tools import tool
from pathlib import Path


BASE_DIR = Path("documents")

@tool
def find_file(filename: str) -> str:
    """
    Search for a file inside the documents folder.
    Returns the matching filename if found.
    """

    print(f"TOOL: find_file({filename})")

    for file in BASE_DIR.rglob("*"):
        if file.is_file():
            if filename.lower() in file.name.lower():
                return file.name

    return "NOT_FOUND"


@tool
def read_file(filename: str) -> str:
    """
    Read a text file and return its contents.
    """
    print(f"TOOL CALLED: read_file({filename})")

    path = BASE_DIR / filename  

    if not path.exists():
        return f"File '{filename}' was not found."

    return path.read_text(encoding="utf-8")