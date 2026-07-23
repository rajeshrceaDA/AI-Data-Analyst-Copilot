import streamlit as st
import json
import os


# ==========================================
# Load Profile
# ==========================================

def load_profile():

    if os.path.exists("master_profile.json"):

        with open("master_profile.json", "r", encoding="utf-8") as file:

            return json.load(file)

    return {}


# ==========================================
# Save Profile
# ==========================================

def save_profile(profile):

    with open("master_profile.json", "w", encoding="utf-8") as file:

        json.dump(profile, file, indent=4)


# ==========================================
# Main Profile Page
# ==========================================

def show_profile():

    profile = load_profile()

    st.title("👤 My Profile")

    st.write("Complete your professional profile.")

    # ==========================================
    # Personal Information
    # ==========================================

    st.header("👤 Personal Information")

    name = st.text_input(
        "Full Name",
        value=profile.get("name", "")
    )

    email = st.text_input(
        "Email",
        value=profile.get("email", "")
    )

    phone = st.text_input(
        "Mobile Number",
        value=profile.get("phone", "")
    )

    location = st.text_input(
        "Location",
        value=profile.get("location", "")
    )

    # ==========================================
    # Professional Links
    # ==========================================

    st.header("🌐 Professional Links")

    linkedin = st.text_input(
        "LinkedIn",
        value=profile.get("linkedin", "")
    )

    github = st.text_input(
        "GitHub",
        value=profile.get("github", "")
    )

    portfolio = st.text_input(
        "Portfolio Website",
        value=profile.get("portfolio", "")
    )

    # ==========================================
    # Professional Information
    # ==========================================

    st.header("💼 Professional Information")

    designation = st.text_input(
        "Current Designation",
        value=profile.get("designation", "")
    )

    company = st.text_input(
        "Current Company",
        value=profile.get("company", "")
    )

    experience = st.text_input(
        "Total Experience",
        value=profile.get("experience", "")
    )

    headline = st.text_input(
        "LinkedIn Headline",
        value=profile.get("headline", "")
    )

    career_goal = st.text_area(
        "Professional Summary",
        value=profile.get("career_goal", ""),
        height=150
    )

    # ==========================================
    # Education
    # ==========================================

    st.header("🎓 Education")

    degree = st.text_input(
        "Degree",
        value=profile.get("degree", "")
    )

    college = st.text_input(
        "College",
        value=profile.get("college", "")
    )

    passing_year = st.text_input(
        "Passing Year",
        value=profile.get("passing_year", "")
    )

    percentage = st.text_input(
        "Percentage / CGPA",
        value=profile.get("percentage", "")
    )

    # ==========================================
    # Work Experience
    # ==========================================

    st.header("💼 Work Experience")

    job_title = st.text_input(
        "Job Title",
        value=profile.get("job_title", "")
    )

    company_name = st.text_input(
        "Company Name",
        value=profile.get("company_name", "")
    )

    start_date = st.text_input(
        "Start Date (MM/YYYY)",
        value=profile.get("start_date", "")
    )

    end_date = st.text_input(
        "End Date / Present",
        value=profile.get("end_date", "")
    )

    responsibilities = st.text_area(
        "Key Responsibilities",
        value=profile.get("responsibilities", ""),
        height=150
    )

    achievements = st.text_area(
        "Achievements",
        value=profile.get("achievements", ""),
        height=120
    )

    # ==========================================
    # Skills
    # ==========================================

    st.header("🛠 Technical Skills")

    skills = st.multiselect(

        "Select Skills",

        [
            "SQL",
            "MySQL",
            "PostgreSQL",
            "Advanced Excel",
            "Power BI",
            "Power Query",
            "DAX",
            "Python",
            "Pandas",
            "NumPy",
            "Statistics",
            "Git",
            "GitHub",
            "Streamlit",
            "Machine Learning"
        ],

        default=profile.get("skills", [])
    )

    # ==========================================
    # Projects
    # ==========================================

    st.header("📂 Projects")

    projects = st.text_area(
        "Projects",
        value=profile.get("projects", ""),
        height=150
    )

    # ==========================================
    # Certifications
    # ==========================================

    st.header("🏆 Certifications")

    certifications = st.text_area(
        "Certifications",
        value=profile.get("certifications", ""),
        height=120
    )

    # ==========================================
    # Languages
    # ==========================================

    st.header("🌐 Languages")

    languages = st.text_input(
        "Languages",
        value=profile.get("languages", "")
    )

    # ==========================================
    # Career Preferences
    # ==========================================

    st.header("🎯 Career Preferences")

    current_salary = st.text_input(
        "Current CTC",
        value=profile.get("current_salary", "")
    )

    expected_salary = st.text_input(
        "Expected CTC",
        value=profile.get("expected_salary", "")
    )

    notice_period = st.text_input(
        "Notice Period",
        value=profile.get("notice_period", "")
    )

    preferred_role = st.text_input(
        "Preferred Job Role",
        value=profile.get("preferred_role", "")
    )

    preferred_location = st.text_input(
        "Preferred Job Location",
        value=profile.get("preferred_location", "")
    )

    # ==========================================
    # Save Profile
    # ==========================================

    st.markdown("---")

    if st.button("💾 Save Profile", use_container_width=True):

        profile = {

            # Personal
            "name": name,
            "email": email,
            "phone": phone,
            "location": location,

            # Links
            "linkedin": linkedin,
            "github": github,
            "portfolio": portfolio,

            # Professional
            "designation": designation,
            "company": company,
            "experience": experience,
            "headline": headline,
            "career_goal": career_goal,

            # Education
            "degree": degree,
            "college": college,
            "passing_year": passing_year,
            "percentage": percentage,

            # Experience
            "job_title": job_title,
            "company_name": company_name,
            "start_date": start_date,
            "end_date": end_date,
            "responsibilities": responsibilities,
            "achievements": achievements,

            # Skills
            "skills": skills,

            # Projects
            "projects": projects,

            # Certifications
            "certifications": certifications,

            # Languages
            "languages": languages,

            # Career
            "current_salary": current_salary,
            "expected_salary": expected_salary,
            "notice_period": notice_period,
            "preferred_role": preferred_role,
            "preferred_location": preferred_location

        }

        save_profile(profile)

        st.success("✅ Profile Saved Successfully")

        st.balloons()