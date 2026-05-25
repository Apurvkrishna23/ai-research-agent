from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage

def run_planner(topic: str) -> list:
    llm = ChatGroq(model="llama-3.3-70b-versatile")
    
    prompt = f"""
    You are a research planner. Your job is to break down a research topic 
    into exactly 3 focused sub-questions that will help gather comprehensive 
    information about the topic.
    
    Topic: {topic}
    
    Return ONLY a numbered list of 3 sub-questions, nothing else.
    Example format:
    1. What are the latest developments in X?
    2. How is X being used in industry?
    3. What are the future predictions for X?
    """
    
    response = llm.invoke([HumanMessage(content=prompt)])
    
    # Parse the numbered list into a Python list
    lines = response.content.strip().split("\n")
    questions = [line.split(". ", 1)[1] for line in lines if line.strip()]
    
    print("🧠 Planner created these sub-questions:")
    for q in questions:
        print(f"   → {q}")
    
    return questions