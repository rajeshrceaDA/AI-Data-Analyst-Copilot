import streamlit as st
from modules.profile import show_profile
from modules.resume import show_resume
from modules.ats_checker import show_ats_checker
# ----------------------------
# Page Configuration
# -------------------
# ---------
st.set_page_config(
    page_title="AI Data Analyst Copilot",
    page_icon="📊",
    layout="wide"
)

# ----------------------------
# Sidebar
# ----------------------------

st.sidebar.title("📊 AI Data Analyst Copilot")

menu = st.sidebar.radio(
    "Select Module",
    [
        "👤 My Profile",
        "🏠 Dashboard",
        "📄 Resume Generator",
        "🎯 ATS Checker",
        "📋 JD Analyzer",
        "📈 Skill Gap Analysis",
        "💼 Job Tracker",
        "⚙️ Settings"
    ]
)

# ----------------------------
# Dashboard
# ----------------------------
if menu == "👤 My Profile":
    show_profile()
    
elif menu == "🏠 Dashboard":

    st.title("🚀 AI Data Analyst Copilot")

    st.write("### Welcome Rajesh 👋")

elif menu == "📄 Resume Generator":
    show_resume()

elif menu == "🎯 ATS Checker":
    show_ats_checker()

elif menu == "📋 JD Analyzer":
    st.title("📋 JD Analyzer")
    st.info("Coming Soon")

elif menu == "📈 Skill Gap Analysis":
    st.title("📈 Skill Gap Analysis")
    st.info("Coming Soon")

elif menu == "💼 Job Tracker":
    st.title("💼 Job Tracker")
    st.info("Coming Soon")

elif menu == "⚙️ Settings":
    st.title("⚙️ Settings")
    st.info("Coming Soon")    
