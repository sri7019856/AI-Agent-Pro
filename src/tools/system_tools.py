
from datetime import datetime
from langchain_core.tools import tool


@tool
def current_time() -> str:
    """
    Returns the current local date and time.
    """

    return datetime.now().strftime("%d-%m-%Y %H:%M:%S")