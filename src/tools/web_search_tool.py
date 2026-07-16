from tavily import TavilyClient

API_KEY = "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"

client = TavilyClient(api_key=API_KEY)


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