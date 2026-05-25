import json
import os
import hashlib

MEMORY_FILE = "research_memory.json"

def _load_memory() -> dict:
    """Load memory from JSON file"""
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    return {}

def _save_memory(memory: dict):
    """Save memory to JSON file"""
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=2)

def save_report(topic: str, report: str):
    """Save a research report to memory"""
    memory = _load_memory()
    topic_id = hashlib.md5(topic.lower().encode()).hexdigest()
    memory[topic_id] = {
        "topic": topic,
        "report": report
    }
    _save_memory(memory)
    print(f"\n💾 Report saved to memory: {topic}")

def find_similar_report(topic: str) -> str | None:
    """Check if we already have research on a similar topic"""
    memory = _load_memory()
    topic_lower = topic.lower()

    for item in memory.values():
        saved_topic = item["topic"].lower()

        # Check if topics are similar (share key words)
        saved_words = set(saved_topic.split())
        query_words = set(topic_lower.split())
        common_words = saved_words & query_words

        # Remove common filler words
        fillers = {"the", "a", "an", "in", "of", "and", "for", "to", "is"}
        common_words -= fillers

        if len(common_words) >= 2:
            print(f"\n🧠 Found similar research in memory!")
            print(f"   Cached topic: '{item['topic']}'")
            return item["report"]

    return None

def list_all_reports() -> list:
    """List all saved research topics"""
    memory = _load_memory()
    return [item["topic"] for item in memory.values()]