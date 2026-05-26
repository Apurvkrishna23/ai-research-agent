import warnings
warnings.filterwarnings("ignore")

import os
import streamlit as st
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API Keys
groq_api_key = os.getenv("GROQ_API_KEY")
tavily_api_key = os.getenv("TAVILY_API_KEY")

if groq_api_key:
    os.environ["GROQ_API_KEY"] = groq_api_key

if tavily_api_key:
    os.environ["TAVILY_API_KEY"] = tavily_api_key

# Import agents
from agents.planner import run_planner
from agents.researcher import run_researcher
from agents.summarizer import run_summarizer
from agents.writer import run_writer

# Import memory functions
from memory.memory import (
    save_report,
    find_similar_report,
    list_all_reports
)

# ─────────────────────────────────────────────
# PAGE CONFIG
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="AI Research Agent",
    page_icon="🔬",
    layout="wide"
)

# ─────────────────────────────────────────────
# CUSTOM CSS
# ─────────────────────────────────────────────
st.markdown("""
<style>
.main-title {
    font-size: 3rem;
    font-weight: 700;
    color: #4F8BF9;
}

.subtitle {
    font-size: 1.2rem;
    color: #AAAAAA;
    margin-bottom: 2rem;
}

.report-box {
    background-color: #111827;
    padding: 1.5rem;
    border-radius: 12px;
    border: 1px solid #333;
}

.memory-box {
    background-color: #0F5132;
    padding: 1rem;
    border-radius: 10px;
    margin-bottom: 1rem;
}

.agent-box {
    background-color: #1E1E1E;
    padding: 0.8rem;
    border-radius: 10px;
    margin-bottom: 0.5rem;
}
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# HEADER
# ─────────────────────────────────────────────
st.markdown(
    '<div class="main-title">🔬 AI Research Agent</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Autonomous multi-agent AI system for deep web research and report generation.</div>',
    unsafe_allow_html=True
)

# ─────────────────────────────────────────────
# SIDEBAR
# ─────────────────────────────────────────────
with st.sidebar:
    st.header("📚 Research History")

    previous_reports = list_all_reports()

    if previous_reports:
        for report in previous_reports:
            st.markdown(f"- {report}")
    else:
        st.info("No previous reports found.")

    st.markdown("---")

    st.header("⚙️ Agent Pipeline")

    st.markdown("""
🧠 Planner Agent  
🔍 Researcher Agent  
📝 Summarizer Agent  
✍️ Writer Agent  
💾 Memory System
""")

# ─────────────────────────────────────────────
# INPUT
# ─────────────────────────────────────────────
topic = st.text_input(
    "Enter a research topic:",
    placeholder="e.g. Future of AI Agents in Healthcare"
)

research_button = st.button("🚀 Start Research")

# ─────────────────────────────────────────────
# RESEARCH FLOW
# ─────────────────────────────────────────────
if research_button:

    if not topic:
        st.warning("Please enter a topic.")
        st.stop()

    # Check memory
    st.info("🔎 Checking memory for similar reports...")

    cached_report = find_similar_report(topic)

    if cached_report:
        st.success("⚡ Found similar report in memory!")

        st.markdown('<div class="memory-box">', unsafe_allow_html=True)
        st.markdown(cached_report)
        st.markdown('</div>', unsafe_allow_html=True)

    else:

        # Planner
        with st.status("🧠 Planner Agent Running...", expanded=True):
            questions = run_planner(topic)

            st.markdown("### Generated Research Questions")
            for q in questions:
                st.markdown(f"- {q}")

        # Researcher
        with st.status("🔍 Researcher Agent Searching Web...", expanded=True):
            research_data = run_researcher(questions)

            st.success("Research completed.")

        # Summarizer
        with st.status("📝 Summarizer Agent Extracting Insights...", expanded=True):
            summaries = run_summarizer(research_data)

            st.success("Summaries created.")

        # Writer
        with st.status("✍️ Writer Agent Writing Report...", expanded=True):
            final_report = run_writer(topic, summaries)

            st.success("Final report generated.")

        # Save to memory
        save_report(topic, final_report)

        # Display report
        st.markdown("## 📄 Final Research Report")

        st.markdown('<div class="report-box">', unsafe_allow_html=True)
        st.markdown(final_report)
        st.markdown('</div>', unsafe_allow_html=True)

        # Download
        st.download_button(
            label="⬇️ Download Report",
            data=final_report,
            file_name=f"{topic.replace(' ', '_')}_report.txt",
            mime="text/plain"
        )

# ─────────────────────────────────────────────
# FOOTER
# ─────────────────────────────────────────────
st.markdown("---")
st.caption("Built using LangGraph, LangChain, Groq LLaMA 3.3, Tavily API, and Streamlit.")