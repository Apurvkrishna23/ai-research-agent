from langchain_groq import ChatGroq
from langchain_tavily import TavilySearch

def run_researcher(questions: list) -> list:
    search_tool = TavilySearch(max_results=2)
    
    all_results = []
    
    print("\n🔍 Researcher searching for each sub-question...")
    
    for question in questions:
        print(f"\n   Searching: {question}")
        results = search_tool.invoke(question)
        
        all_results.append({
            "question": question,
            "results": results
        })
    
    return all_results