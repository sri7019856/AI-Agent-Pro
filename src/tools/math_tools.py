from langchain_core.tools import tool


@tool
def multiply(a: int, b: int) -> int:
    """
    Multiply two integers.
    """
    return a * b


@tool
def add(a: int, b: int) -> int:
    """
    Add two integers.
    """
    return a + b


@tool
def divide(a: float, b: float) -> float:
    """Divide two numbers."""
    return a / b


@tool
def subtract(a: int, b: int) -> int:
    """Subtract two integers."""
    return a - b
