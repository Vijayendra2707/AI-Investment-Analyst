from langchain_tavily import TavilySearch

search_tool = TavilySearch(
    max_results=5,
    topic="news"
)

def search_news(query: str):
    return search_tool.invoke(query)