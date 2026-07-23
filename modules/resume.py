import streamlit as st
import json
import os

from utils.docx_export import export_resume_to_docx
from utils.ai_engine import ask_ai
# =====================================================
# Load Profile
# =====================================================

def load_profile():

    # Personal Profile
    if os.path.exists("master_profile.json"):

        with open("master_profile.json", "r", encoding="utf-8") as file:
            return json.load(file)

    # Template Profile
    if os.path.exists("master_profile_template.json"):

        with open("master_profile_template.json", "r", encoding="utf-8") as file:
            profile = json.load(file)

        with open("master_profile.json", "w", encoding="utf-8") as f:
            json.dump(profile, f, indent=4, ensure_ascii=False)

        return profile

    return None


# =====================================================
# Resume Header
# =====================================================

def show_header(profile):

    st.title(profile.get("name", ""))

    if profile.get("designation", ""):
        st.subheader(profile.get("designation", ""))

    st.write(
        f"📧 {profile.get('email', '')} | "
        f"📱 {profile.get('phone', '')} | "
        f"📍 {profile.get('location', '')}"
    )

    linkedin = profile.get("linkedin", "")

    github = profile.get("github", "")

    if linkedin:
        st.write(f"🔗 LinkedIn: {linkedin}")

    if github:
        st.write(f"💻 GitHub: {github}")

    st.divider()


# =====================================================
# Professional Summary
# =====================================================

def show_summary(profile):

    # -----------------------------
    # Session State
    # -----------------------------
    if "improved_summary" not in st.session_state:
        st.session_state.improved_summary = ""

    summary = profile.get("career_goal", "")

    if summary.strip() == "":
        return

    st.markdown("## Professional Summary")

    st.write(summary)

    st.markdown("---")

    # -----------------------------
    # AI Prompt
    # -----------------------------
    prompt = f"""
You are an expert ATS Resume Writer.

Rewrite the following professional summary.

Rules:
- Return ONLY the improved summary.
- Do NOT add headings.
- Do NOT write 'Professional Summary'.
- Do NOT explain your changes.
- Do NOT include bullet points.
- Do NOT include Key Improvements.
- Keep it under 100 words.
- ATS Friendly.
- Professional English.
- Keep the original meaning.
- Do not add fake experience or fake skills.

Original Summary:

{summary}
"""

    # -----------------------------
    # AI Generate Button
    # -----------------------------
    if st.button("✨ Improve with AI"):

        with st.spinner("🤖 AI is improving your summary..."):

            try:

                st.session_state.improved_summary = ask_ai(prompt)

                st.success("✅ AI Summary Generated Successfully!")

            except Exception as e:

                st.error(f"AI Error: {e}")

    # -----------------------------
    # Show AI Result
    # -----------------------------
    if st.session_state.improved_summary != "":

        st.text_area(
            "🤖 AI Generated Summary",
            value=st.session_state.improved_summary,
            height=220,
            key="ai_summary_box"
        )

        col1, col2 = st.columns(2)

        # -----------------------------
        # Replace Button
        # -----------------------------
        with col1:

            if st.button("✅ Replace Original Summary"):

                profile["career_goal"] = st.session_state.improved_summary

                with open(
                    "master_profile.json",
                    "w",
                    encoding="utf-8"
                ) as f:

                    json.dump(
                        profile,
                        f,
                        indent=4,
                        ensure_ascii=False
                    )

                st.session_state.improved_summary = ""

                st.success("✅ Summary Updated Successfully!")

                st.rerun()

        # -----------------------------
        # Clear Button
        # -----------------------------
        with col2:

            if st.button("❌ Clear AI Result"):

                st.session_state.improved_summary = ""

                st.rerun()
    st.divider()


# =====================================================
# Skills
# =====================================================

def show_skills(profile):

    skills = profile.get("skills", [])

    if len(skills) == 0:
        return

    st.markdown("## Technical Skills")

    col1, col2, col3 = st.columns(3)

    for index, skill in enumerate(skills):

        if index % 3 == 0:
            col1.write(f"✅ {skill}")

        elif index % 3 == 1:
            col2.write(f"✅ {skill}")

        else:
            col3.write(f"✅ {skill}")

    st.divider()


# =====================================================
# Education
# =====================================================

def show_education(profile):

    st.markdown("## Education")

    st.write(
        "**Degree :**",
        profile.get("degree","")
    )

    st.write(
        "**College :**",
        profile.get("college","")
    )

    st.write(
        "**Passing Year :**",
        profile.get("passing_year","")
    )

    st.write(
        "**Percentage :**",
        profile.get("percentage","")
    )

    st.divider()

# =====================================================
# Work Experience
# =====================================================

# =====================================================
# Work Experience
# =====================================================

def show_experience(profile):

    st.markdown("## Work Experience")

    has_experience = False

    for i in [1, 2]:

        suffix = "" if i == 1 else "_2"

        job_title = profile.get(f"job_title{suffix}", "")
        company = profile.get(f"company_name{suffix}", "")
        start = profile.get(f"start_date{suffix}", "")
        end = profile.get(f"end_date{suffix}", "")
        responsibilities = profile.get(f"responsibilities{suffix}", "")
        achievements = profile.get(f"achievements{suffix}", "")

        if (
            job_title == ""
            and company == ""
            and responsibilities == ""
            and achievements == ""
        ):
            continue

        has_experience = True

        st.markdown(f"### {job_title}")

        st.write(company)

        st.caption(f"{start}  -  {end}")

        if responsibilities != "":
            st.markdown("**Key Responsibilities**")
            st.write(responsibilities)

        if achievements != "":
            st.markdown("**Achievements**")
            st.write(achievements)

        st.divider()

    if not has_experience:
        st.info("No Work Experience Added")


# =====================================================
# Certifications
# =====================================================

def show_certifications(profile):

    certifications = profile.get("certifications", "")

    if certifications == "":
        return

    st.markdown("## Certifications")

    st.write(certifications)

    st.divider()


# =====================================================
# Projects
# =====================================================

def show_projects(profile):

    st.markdown("## Projects")

    has_project = False

    for i in [1, 2, 3]:

        name = profile.get(f"project_name_{i}", "")
        tech = profile.get(f"project_tech_{i}", "")
        duration = profile.get(f"project_duration_{i}", "")
        github = profile.get(f"project_github_{i}", "")
        description = profile.get(f"project_description_{i}", "")

        if (
            name == ""
            and tech == ""
            and description == ""
        ):
            continue

        has_project = True

        st.markdown(f"### {name}")

        if tech:
            st.write(f"**Technologies:** {tech}")

        if duration:
            st.write(f"**Duration:** {duration}")

        if github:
            st.write(f"**GitHub:** {github}")

        if description:
            st.write("**Project Description**")
            st.write(description)

        st.divider()

    if not has_project:
        st.info("No Projects Added")


# =====================================================
# Languages
# =====================================================

def show_languages(profile):

    languages = profile.get("languages", "")

    if languages == "":
        return

    st.markdown("## Languages")

    st.write(languages)

    st.divider()

# =====================================================
# Resume Preview
# =====================================================

def resume_preview(profile):

    show_header(profile)

    show_summary(profile)

    show_skills(profile)

    show_experience(profile)

    show_education(profile)

    show_projects(profile)

    show_certifications(profile)

    show_languages(profile)


# =====================================================
# Main Resume Function
# =====================================================

def show_resume():

    st.title("📄 Resume Generator")

    # ==============================
    # Resume Template Selector
    # ==============================

    template = st.selectbox(
        "📄 Select Resume Template",
        [
            "Professional",
            "Modern (Coming Soon)",
            "Executive (Coming Soon)"
        ]
    )

    if template != "Professional":
        st.info("🚧 This template will be available in a future update.")
        return

    profile = load_profile()

    # Create output folder if it doesn't exist
    os.makedirs("generated_resume", exist_ok=True)

    if profile is None:
        st.warning("Please complete Profile first.")
        return

    st.success("✅ Profile Loaded Successfully")

    st.divider()
    st.subheader("📄 Resume Preview")
    st.divider()

    resume_preview(profile)

    st.markdown("---")

    st.subheader("Export Resume")

    col1, col2 = st.columns(2)

    with col1:

        if st.button("📄 Generate DOCX Resume", use_container_width=True):

            output_file = os.path.join(
                "generated_resume",
                "Resume.docx"
            )

            export_resume_to_docx(profile, output_file)

            st.success("✅ Resume Generated Successfully!")

            with open(output_file, "rb") as file:

                st.download_button(
                    label="⬇ Download DOCX",
                    data=file,
                    file_name="Rajesh_Kumar_Resume.docx",
                    mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                    use_container_width=True
                )

    with col2:

        st.button(
            "📕 Download PDF (Coming Soon)",
            use_container_width=True,
            disabled=True
        )

    st.info(
        """
🚀 Upcoming Features

• ATS Resume Generator

• Multiple Resume Templates

• PDF Export

• DOCX Export

• AI Resume Optimizer

• Resume Version Manager

"""
    )

   