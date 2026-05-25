import warnings
warnings.filterwarnings("ignore")

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import streamlit as st
from dotenv import load_dotenv

load_dotenv()

# Load API keys from Railway environment variables
groq_api_key = os.getenv("GROQ_API_KEY")
tavily_api_key = os.getenv("TAVILY_API_KEY")

# Set them into environment
if groq_api_key:
    os.environ["GROQ_API_KEY"] = groq_api_key

if tavily_api_key:
    os.environ["TAVILY_API_KEY"] = tavily_api_key

# rest of imports
from agents.planner import run_planner
from agents.researcher import run_researcher
from agents.summarizer import run_summarizer
from agents.writer import run_writer
from memory.memory import save_report, find_similar_report, list_all_reports

# ─── Page Config ───────────────────────────────────────────
st.set_page_config(
    page_title="AI Research Agent",
    page_icon="🔬",
    layout="wide"
)

# ─── Custom Styling ────────────────────────────────────────
st.markdown("""
    <style>
    .main-title {
        font-size: 2.5rem;
        font-weight: 700;
        color: #1a1a2e;
    }
    .subtitle {
        font-size: 1.1rem;
        color: #666;
        margin-bottom: 2rem;
    }
    .agent-box {
        background: #f0f4ff;
        border-left: 4px solid #4361ee;
        padding: 0.8rem 1rem;
        border-radius: 0 8px 8px 0;
        margin: 0.5rem 0;
    }
    .memory-box {
        background: #f0fff4;
        border-left: 4px solid #2ecc71;
        padding: 0.8rem 1rem;
        border-radius: 0 8px 8px 0;
        margin: 0.5rem 0;
    }
    .report-box {
        background: #ffffff;
        border: 1px solid #e0e0e0;
        border-radius: 12px;
        padding: 2rem;
        margin-top: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

# ─── Header ────────────────────────────────────────────────
st.markdown('<p class="main-title">🔬 AI Research Agent</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Multi-agent AI that autonomously researches any topic and generates professional reports</p>', unsafe_allow_html=True)

# ─── Sidebar ───────────────────────────────────────────────
with st.sidebar:
    st.markdown("### 📚 Research History")
    st.markdown("---")
    
    past_topics = list_all_reports()
    
    if past_topics:
        for topic in past_topics:
            if st.button(f"📄 {topic[:35]}...", key=topic):
                st.session_state.selected_topic = topic
    else:
        st.info("No research history yet. Run your first research!")
    
    st.markdown("---")
    st.markdown("### ⚙️ Agent Pipeline")
    st.markdown("🧠 **Planner** → breaks topic down")
    st.markdown("🔍 **Researcher** → searches the web")
    st.markdown("📝 **Summarizer** → extracts insights")
    st.markdown("✍️ **Writer** → compiles report")

# ─── Main Input ────────────────────────────────────────────
col1, col2 = st.columns([4, 1])

with col1:
    topic = st.text_input(
        "Research Topic",
        placeholder="e.g. latest trends in agentic AI 2025",
        label_visibility="collapsed"
    )

with col2:
    research_btn = st.button("🔍 Research", type="primary", use_container_width=True)

# ─── Run Research ──────────────────────────────────────────
if research_btn and topic:
    
    # Check memory first
    with st.spinner("Checking memory..."):
        cached = find_similar_report(topic)
    
    if cached:
        st.markdown('<div class="memory-box">⚡ <b>Found in memory!</b> Returning cached report instantly.</div>', unsafe_allow_html=True)
        st.markdown("---")
        st.markdown("## 📄 Research Report")
        st.markdown('<div class="report-box">', unsafe_allow_html=True)
        st.markdown(cached)
        st.markdown('</div>', unsafe_allow_html=True)
    
    else:
        st.markdown("**🤖 Agent Pipeline Running...**")
        st.markdown("")
        
        # Planner
        with st.status("🧠 Planner Agent thinking...", expanded=True) as status:
            st.write("Breaking your topic into focused sub-questions...")
            questions = run_planner(topic)
            for q in questions:
                st.write(f"→ {q}")
            status.update(label="🧠 Planner Agent ✅", state="complete")
        
        # Researcher
        with st.status("🔍 Researcher Agent searching...", expanded=True) as status:
            for q in questions:
                st.write(f"Searching: {q[:60]}...")
            research_data = run_researcher(questions)
            status.update(label="🔍 Researcher Agent ✅", state="complete")
        
        # Summarizer
        with st.status("📝 Summarizer Agent extracting insights...", expanded=True) as status:
            st.write("Reading and summarizing search results...")
            summaries = run_summarizer(research_data)
            status.update(label="📝 Summarizer Agent ✅", state="complete")
        
        # Writer
        with st.status("✍️ Writer Agent compiling report...", expanded=True) as status:
            st.write("Writing your professional research report...")
            final_report = run_writer(topic, summaries)
            status.update(label="✍️ Writer Agent ✅", state="complete")
        
        # Save to memory
        save_report(topic, final_report)
        
        st.success("✅ Research complete! Report saved to memory.")
        st.markdown("---")
        
        # Display report
        st.markdown("## 📄 Research Report")
        st.markdown('<div class="report-box">', unsafe_allow_html=True)
        st.markdown(final_report)
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Download button
        st.download_button(
            label="⬇️ Download Report",
            data=final_report,
            file_name=f"research_{topic[:30].replace(' ', '_')}.txt",
            mime="text/plain"
        )

elif research_btn and not topic:
    st.warning("Please enter a research topic first!")

# ─── Empty State ───────────────────────────────────────────
if not research_btn:
    st.markdown("---")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("### 🚀 How it works")
        st.markdown("Type any topic above and click Research. The AI agents will automatically search the web and compile a report.")
    
    with col2:
        st.markdown("### ⚡ Smart Memory")
        st.markdown("Already researched a topic? The agent remembers and returns results instantly without repeating searches.")
    
    with col3:
        st.markdown("### 📥 Download")
        st.markdown("Every report can be downloaded as a text file to save and share with anyone.")