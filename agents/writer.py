from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage

def run_writer(topic: str, summaries: list) -> str:
    llm = ChatGroq(model="llama-3.3-70b-versatile")
    
    # Format summaries for the prompt
    formatted = ""
    for item in summaries:
        formatted += f"\nQuestion: {item['question']}\n"
        formatted += f"Insights: {item['summary']}\n"
        formatted += "-" * 40
    
    prompt = f"""
    You are a professional research writer. Using the research insights below,
    write a comprehensive, well-structured research report on: {topic}
    
    Research Insights:
    {formatted}
    
    Format the report with:
    - A clear title
    - An introduction paragraph
    - Key Findings section with subheadings
    - A conclusion paragraph
    
    Make it professional and informative.
    """
    
    print("\n✍️  Writer compiling final report...")
    
    response = llm.invoke([HumanMessage(content=prompt)])
    return response.content