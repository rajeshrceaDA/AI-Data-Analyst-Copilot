import streamlit as st
from utils.ai_engine import ask_ai

# ==========================================
# AI Chat Module
# ==========================================

def show_ai_chat():

    st.title("🤖 AI Data Analyst Assistant")

    st.write(
        "Ask anything about SQL, Power BI, Excel, Python, Statistics, Resume, ATS, Business Analysis, or Interviews."
    )

    st.divider()

    # -----------------------------
    # Initialize Chat History
    # -----------------------------

    if "chat_history" not in st.session_state:

        st.session_state.chat_history = [

            {
                "role": "assistant",
                "content": "👋 Hello! I'm your AI Data Analyst Copilot.\n\nHow can I help you today?"
            }

        ]

    # -----------------------------
    # Display Messages
    # -----------------------------

    for message in st.session_state.chat_history:

        with st.chat_message(message["role"]):

            st.markdown(message["content"])

    # -----------------------------
    # User Input
    # -----------------------------

    prompt = st.chat_input("Ask anything...")

    if prompt:

        st.session_state.chat_history.append(
            {
                "role": "user",
                "content": prompt
            }
        )

        with st.chat_message("user"):

            st.markdown(prompt)

        with st.chat_message("assistant"):

            with st.spinner("Thinking..."):

                messages = [
                    {
                        "role": "system",
                        "content": """
        You are an Expert Senior Data Analyst.

        Help users with:

        - SQL
        - MySQL
        - Power BI
        - DAX
        - Excel
        - Python
        - Statistics
        - Resume
        - ATS
        - Interview Preparation
        - Business Analysis
        - Dashboard Design

        Always answer in a practical, structured and beginner-friendly way.
        Give examples whenever possible.
        """
                    }
                ]

                # Add complete conversation history
                messages.extend(st.session_state.chat_history)

                # Ask AI
                reply = ask_ai(messages)

                st.markdown(reply)

        st.session_state.chat_history.append(
            {
                "role": "assistant",
                "content": reply
            }
        )