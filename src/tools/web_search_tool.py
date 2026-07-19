from tavily import TavilyClient

from src.config import TAVILY_API_KEY

client = TavilyClient(api_key=TAVILY_API_KEY)

def web_search(query: str):
    """Search the web and return concise results."""

    result = client.search(
        query=query,
        max_results=2,
    )

    output = ""

    for item in result["results"]:
        output += (
            f"Title: {item['title']}\n"
            f"Summary: {item['content'][:150]}...\n"
            f"Source: {item['url']}\n\n"
        )

    return output