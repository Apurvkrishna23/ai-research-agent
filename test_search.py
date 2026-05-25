from dotenv import load_dotenv
from tavily import TavilyClient

load_dotenv()

client = TavilyClient()

results = client.search("latest trends in agentic AI 2025")

for r in results["results"]:
    print(r["title"])
    print(r["url"])
    print()