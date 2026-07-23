import streamlit as st
import json
import os

from utils.resume_parser import profile_to_resume_text
from utils.jd_parser import parse_job_description
from utils.ats_engine import calculate_ats_score


# ==========================================
# Load Profile
# ==========================================

def load_profile():

    if not os.path.exists("master_profile.json"):
        return None

    with open("master_profile.json", "r", encoding="utf-8") as file:
        return json.load(file)


# ==========================================
# ATS Checker
# ==========================================

def show_ats_checker():

    st.title("🎯 ATS Resume Checker")

    st.write(
        "Analyze your Master Resume against a Job Description."
    )

    st.divider()

    profile = load_profile()

    if profile is None:

        st.warning("Please complete your profile first.")

        return

    st.success("✅ Master Resume Loaded")

    # -----------------------------------
    # Job Description
    # -----------------------------------

    st.subheader("📄 Job Description")

    uploaded_jd = st.file_uploader(
        "Upload Job Description",
        type=["pdf", "docx", "txt"]
    )

    jd_text = st.text_area(
        "OR Paste Job Description",
        height=200
    )

    st.divider()

    if st.button("🚀 Analyze ATS", use_container_width=True):

        resume_text = profile_to_resume_text(profile)

        if uploaded_jd is not None:

            jd_text = parse_job_description(uploaded_jd)

        if jd_text.strip() == "":

            st.warning("Please upload or paste a Job Description.")

            return

        result = calculate_ats_score(
            resume_text,
            jd_text
        )

        st.success("Analysis Completed Successfully")

        st.metric(
            "ATS Score",
            f"{result['score']}%"
        )

        col1, col2 = st.columns(2)

        with col1:

            st.subheader("✅ Matched Keywords")

            if result["matched"]:

                for keyword in result["matched"]:
                    st.success(keyword)

            else:

                st.info("No keywords matched.")

        with col2:

            st.subheader("❌ Missing Keywords")

            if result["missing"]:

                for keyword in result["missing"]:
                    st.error(keyword)

            else:

                st.success("No missing keywords.")