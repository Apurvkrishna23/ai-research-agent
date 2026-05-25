from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage

def run_summarizer(research_data: list) -> list:
    llm = ChatGroq(model="llama-3.3-70b-versatile")
    
    summaries = []
    
    print("\n📝 Summarizer extracting key insights...")
    
    for item in research_data:
        question = item["question"]
        results = item["results"]
        
        prompt = f"""
        Based on the following search results, extract the 3 most important 
        insights that answer this question: {question}
        
        Search Results:
        {results}
        
        Return a concise summary in 3-4 sentences.
        """
        
        response = llm.invoke([HumanMessage(content=prompt)])
        
        summaries.append({
            "question": question,
            "summary": response.content
        })
        
        print(f"   ✅ Summarized: {question[:50]}...")
    
    return summaries