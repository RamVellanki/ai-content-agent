import os
import requests
from langchain.tools import Tool
from dotenv import load_dotenv

# 1. Raw search function
def search_web(query, num_results=5):
    """
    Search the web using Serper.dev API based on a query string.
    Returns a list of {title, link, snippet}.
    """
    load_dotenv()
    api_key = os.getenv("SERPER_API_KEY")
    if not api_key:
        raise ValueError("SERPER_API_KEY environment variable not set.")
    
    url = "https://google.serper.dev/search"

    headers = {
        "X-API-KEY": api_key,
        "Content-Type": "application/json"
    }

    payload = {
        "q": query,
        "num": num_results
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        data = response.json()

        results = []
        for item in data.get("organic", [])[:num_results]:
            results.append({
                "title": item.get("title"),
                "link": item.get("link"),
                "snippet": item.get("snippet")
            })
        
        return results

    except Exception as e:
        print(f"Search failed: {e}")
        return []

# 2. LangChain Tool wrapping the search function
web_search_tool = Tool(
    name="web_search_tool",
    description="Useful for finding recent articles, blog posts, or news about a given topic.",
    func=lambda query: str(search_web(query))
)