# 🔬 AI Research Agent

> A multi-agent AI system that autonomously researches any topic and generates professional reports.

🌐 **Live Demo**: https://ai-research-agent-gxzi8parytymx7pxnatmmt.streamlit.app/#global-outlook-and-challenges
---

## 📌 What is this?

This project is a fully autonomous AI research assistant built using a 
multi-agent architecture. You give it any topic, and it automatically 
searches the web, reads articles, extracts insights, and compiles a 
professional research report — all without any human intervention.

---

## 🏗️ Architecture
```
User Input (Topic)
       ↓
🧠 Planner Agent    → breaks topic into 3 focused sub-questions
       ↓
🔍 Researcher Agent → searches the live web for each sub-question
       ↓
📝 Summarizer Agent → extracts key insights from search results
       ↓
✍️  Writer Agent     → compiles everything into a professional report
       ↓
💾 Memory System    → saves report for instant retrieval next time
```

---

## ✨ Features

- 🤖 Fully autonomous multi-agent pipeline
- 🌐 Live web search on any topic using Tavily API
- 💾 Smart memory — never repeats research it has already done
- ⚡ Instant results for previously researched topics
- 📥 Download reports as text files
- 🎨 Clean dark themed web interface built with Streamlit

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| LangGraph | Multi-agent orchestration |
| LangChain | LLM framework |
| Groq LLaMA 3.3 70B | Language model |
| Tavily API | Live web search |
| Streamlit | Frontend UI |
| Python 3.11 | Core language |
| JSON | Memory/caching system |
| Docker | Containerization |
| Hugging Face Spaces | Deployment |

---

## 🤖 Agent Pipeline Explained

### 🧠 Planner Agent
Takes the user's topic and breaks it down into 3 focused 
sub-questions to ensure comprehensive research coverage.

### 🔍 Researcher Agent  
Takes each sub-question and searches the live web using 
Tavily API, fetching the most relevant and recent articles.

### 📝 Summarizer Agent
Reads through all the raw search results and extracts the 
3 most important insights for each sub-question.

### ✍️ Writer Agent
Takes all the summarized insights and compiles them into 
a well-structured professional report with title, introduction, 
key findings, and conclusion.

### 💾 Memory System
Saves every research report locally. Next time a similar 
topic is searched, it returns the cached report instantly 
without making any API calls.

---

## 📁 Project Structure
```
ai-research-agent/
│
├── agents/
│   ├── planner.py        # breaks topic into sub-questions
│   ├── researcher.py     # searches the web using Tavily
│   ├── summarizer.py     # extracts key insights
│   └── writer.py         # compiles final report
│
├── frontend/
│   └── app.py            # Streamlit web interface
│
├── memory/
│   └── memory.py         # JSON-based caching system
│
├── main.py               # pipeline entry point
├── requirements.txt      # dependencies
└── Dockerfile            # for deployment
```

---

## ⚙️ Run Locally

### 1. Clone the repo
```bash
git clone https://github.com/apurvkrishna23/ai-research-agent
cd ai-research-agent
```

### 2. Create virtual environment
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Create `.env` file with your API keys
```
GROQ_API_KEY=your_groq_key_here
TAVILY_API_KEY=your_tavily_key_here
```

### 5. Run the app
```bash
streamlit run frontend/app.py
```

---

## 🔑 Get Free API Keys

| API | Link | Free Tier |
|---|---|---|
| Groq | [console.groq.com](https://console.groq.com) | ✅ Free |
| Tavily | [tavily.com](https://tavily.com) | ✅ 1000 searches/month free |

---

## 💡 What I Learned

- Building multi-agent AI systems using LangGraph
- Connecting LLMs to real-world tools like web search
- Implementing a memory/caching system for AI applications
- Deploying AI apps using Docker and Hugging Face Spaces
- Designing clean user interfaces with Streamlit

---

## 🚀 Future Improvements

- [ ] Add PDF export for research reports
- [ ] Integrate arXiv API for academic paper search
- [ ] Add email delivery of reports
- [ ] Support for multiple languages
- [ ] Add source credibility scoring

---

## 👤 Author

**Apurv** — [GitHub](https://github.com/apurvkrishna23)

---

## ⭐ If you found this useful, please star the repo!
