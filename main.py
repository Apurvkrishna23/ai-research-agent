import warnings
warnings.filterwarnings("ignore")

from dotenv import load_dotenv
from agents.planner import run_planner
from agents.researcher import run_researcher
from agents.summarizer import run_summarizer
from agents.writer import run_writer
from memory.memory import save_report, find_similar_report, list_all_reports

load_dotenv()

def run_research_pipeline(topic: str):
    print(f"\n{'='*60}")
    print(f"  RESEARCH PIPELINE STARTED")
    print(f"  Topic: {topic}")
    print(f"{'='*60}")
    
    # Step 0: Check memory first
    print("\n🔎 Checking memory for similar research...")
    cached_report = find_similar_report(topic)
    
    if cached_report:
        print("\n✅ Found in memory! Returning cached report...")
        print(f"\n{'='*60}")
        print("  REPORT FROM MEMORY")
        print(f"{'='*60}\n")
        print(cached_report)
        return cached_report
    
    print("   Nothing found in memory, starting fresh research...")
    
    # Step 1: Planner
    questions = run_planner(topic)
    
    # Step 2: Researcher
    research_data = run_researcher(questions)
    
    # Step 3: Summarizer
    summaries = run_summarizer(research_data)
    
    # Step 4: Writer
    final_report = run_writer(topic, summaries)
    
    # Step 5: Save to memory
    save_report(topic, final_report)
    
    print(f"\n{'='*60}")
    print("  FINAL RESEARCH REPORT")
    print(f"{'='*60}\n")
    print(final_report)
    
    return final_report

if __name__ == "__main__":
    # Show existing memory
    existing = list_all_reports()
    if existing:
        print(f"\n📚 Topics already in memory: {existing}")
    
    # First run - will do full research
    run_research_pipeline("latest trends in agentic AI 2025")
    
    print("\n" + "="*60)
    print("  RUNNING AGAIN TO TEST MEMORY")
    print("="*60)
    
    # Second run - should load from memory instantly
    run_research_pipeline("agentic AI trends 2025")