import warnings
warnings.filterwarnings("ignore")

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_tavily import TavilySearch
from langgraph.prebuilt import create_react_agent

load_dotenv()

llm = ChatGroq(model="llama-3.3-70b-versatile")
search_tool = TavilySearch(max_results=3)
tools = [search_tool]

agent = create_react_agent(llm, tools)

def run_agent(topic):
    print(f"\n🔍 Researching: {topic}\n")
    print("-" * 50)
    
    response = agent.invoke({
        "messages": [
            ("user", f"Research this topic and give me a detailed summary: {topic}")
        ]
    })
    
    final_response = response["messages"][-1].content
    print(final_response)

run_agent("latest trends in agentic AI 2025")