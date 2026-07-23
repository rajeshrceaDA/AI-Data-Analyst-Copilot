import streamlit as st
import json
import os


# ==========================================
# Load Profile
# ==========================================

def load_profile():

    # Personal Profile
    if os.path.exists("master_profile.json"):

        with open("master_profile.json", "r", encoding="utf-8") as file:
            return json.load(file)

    # Template Profile
    if os.path.exists("master_profile_template.json"):

        with open("master_profile_template.json", "r", encoding="utf-8") as file:
            profile = json.load(file)

        # First time user ke liye automatically profile create
        with open("master_profile.json", "w", encoding="utf-8") as file:
            json.dump(profile, file, indent=4, ensure_ascii=False)

        return profile

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

    st.subheader("Experience 2")

    job_title_2 = st.text_input(
        "Job Title (2)",
        value=profile.get("job_title_2", "")
    )

    company_name_2 = st.text_input(
        "Company Name (2)",
        value=profile.get("company_name_2", "")
    )

    start_date_2 = st.text_input(
        "Start Date (2)",
        value=profile.get("start_date_2", "")
    )

    end_date_2 = st.text_input(
        "End Date (2)",
        value=profile.get("end_date_2", "")
    )

    responsibilities_2 = st.text_area(
        "Responsibilities (2)",
        value=profile.get("responsibilities_2", ""),
        height=150
    )

    achievements_2 = st.text_area(
        "Achievements (2)",
        value=profile.get("achievements_2", ""),
        height=120
    )

    # ==========================================
    # Skills
    # ==========================================

    st.header("🛠 Technical Skills")

    # Database
    database_skills = st.multiselect(
        "🗄 Database Skills",
        [
            "SQL",
            "MySQL",
            "PostgreSQL",
            "SQL Server",
            "Oracle",
            "SQLite",
            "MongoDB"
        ]
    )

    # Excel
    excel_skills = st.multiselect(
        "📊 Excel Skills",
        [
            "Excel",
            "Advanced Excel",
            "Pivot Table",
            "Pivot Chart",
            "VLOOKUP",
            "HLOOKUP",
            "XLOOKUP",
            "INDEX MATCH",
            "SUMIF",
            "SUMIFS",
            "COUNTIF",
            "COUNTIFS",
            "IF",
            "Conditional Formatting",
            "Data Validation",
            "Text to Columns",
            "Remove Duplicates",
            "Power Query"
        ]
    )

    # BI
    bi_skills = st.multiselect(
        "📈 BI Tools",
        [
            "Power BI",
            "DAX",
            "Power Query",
            "Tableau",
            "Looker Studio",
            "Microsoft Fabric",
            "Dashboard Development",
            "Interactive Dashboards",
            "KPI Dashboard",
            "Executive Dashboard",
            "Data Visualization"
        ]
    )

    # Programming
    programming_skills = st.multiselect(
        "💻 Programming",
        [
            "Python",
            "Pandas",
            "NumPy",
            "Matplotlib",
            "Plotly",
            "Streamlit",
            "Jupyter Notebook",
            "VS Code",
            "Git",
            "GitHub"
        ]
    )

    # Data Analytics
    analytics_skills = st.multiselect(
        "📉 Data Analytics",
        [
            "Data Analysis",
            "Business Analysis",
            "Research Analysis",
            "Data Cleaning",
            "Data Wrangling",
            "Exploratory Data Analysis (EDA)",
            "Statistical Analysis",
            "Business Intelligence",
            "MIS Reporting",
            "KPI Reporting",
            "Data Modeling",
            "Data Mining",
            "Data Validation",
            "ETL",
            "Report Automation",
            "Root Cause Analysis",
            "Trend Analysis",
            "Forecasting"
        ]
    )

    # Version Control
    tools_skills = st.multiselect(
        "🌐 Version Control",
        [
            "Git",
            "GitHub"
        ]
    )

    # Soft Skills
    soft_skills = st.multiselect(
        "🤝 Soft Skills",
        [
            "Communication",
            "Presentation",
            "Problem Solving",
            "Analytical Thinking",
            "Critical Thinking",
            "Decision Making",
            "Leadership",
            "Teamwork",
            "Time Management",
            "Attention to Detail"
        ]
    )

    skills = (
        database_skills
        + excel_skills
        + bi_skills
        + programming_skills
        + analytics_skills
        + tools_skills
        + soft_skills
    )

    # ==========================================
    # Projects
    # ==========================================

    # -------------------------------
    # Project 1
    # -------------------------------

    st.subheader("Project 1")

    project_name_1 = st.text_input(
        "Project Name (1)",
        value=profile.get("project_name_1", "")
    )

    project_tech_1 = st.text_input(
        "Technologies Used (1)",
        value=profile.get("project_tech_1", "")
    )

    project_duration_1 = st.text_input(
        "Project Duration (1)",
        value=profile.get("project_duration_1", "")
    )

    project_github_1 = st.text_input(
        "GitHub Link (1)",
        value=profile.get("project_github_1", "")
    )

    project_description_1 = st.text_area(
        "Project Description (1)",
        value=profile.get("project_description_1", ""),
        height=120
    )

    # -------------------------------
    # Project 2
    # -------------------------------

    st.subheader("Project 2")

    project_name_2 = st.text_input(
        "Project Name (2)",
        value=profile.get("project_name_2", "")
    )

    project_tech_2 = st.text_input(
        "Technologies Used (2)",
        value=profile.get("project_tech_2", "")
    )

    project_duration_2 = st.text_input(
        "Project Duration (2)",
        value=profile.get("project_duration_2", "")
    )

    project_github_2 = st.text_input(
        "GitHub Link (2)",
        value=profile.get("project_github_2", "")
    )

    project_description_2 = st.text_area(
        "Project Description (2)",
        value=profile.get("project_description_2", ""),
        height=120
    )

    # -------------------------------
    # Project 3
    # -------------------------------

    st.subheader("Project 3")

    project_name_3 = st.text_input(
        "Project Name (3)",
        value=profile.get("project_name_3", "")
    )

    project_tech_3 = st.text_input(
        "Technologies Used (3)",
        value=profile.get("project_tech_3", "")
    )

    project_duration_3 = st.text_input(
        "Project Duration (3)",
        value=profile.get("project_duration_3", "")
    )

    project_github_3 = st.text_input(
        "GitHub Link (3)",
        value=profile.get("project_github_3", "")
    )

    project_description_3 = st.text_area(
        "Project Description (3)",
        value=profile.get("project_description_3", ""),
        height=120
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

            # Experience 1
            "job_title": job_title,
            "company_name": company_name,
            "start_date": start_date,
            "end_date": end_date,
            "responsibilities": responsibilities,
            "achievements": achievements,

            # Experience 2
            "job_title_2": job_title_2,
            "company_name_2": company_name_2,
            "start_date_2": start_date_2,
            "end_date_2": end_date_2,
            "responsibilities_2": responsibilities_2,
            "achievements_2": achievements_2,

            # Skills
            "skills": skills,

            # Projects
            "project_name_1": project_name_1,
            "project_tech_1": project_tech_1,
            "project_duration_1": project_duration_1,
            "project_github_1": project_github_1,
            "project_description_1": project_description_1,

            "project_name_2": project_name_2,
            "project_tech_2": project_tech_2,
            "project_duration_2": project_duration_2,
            "project_github_2": project_github_2,
            "project_description_2": project_description_2,

            "project_name_3": project_name_3,
            "project_tech_3": project_tech_3,
            "project_duration_3": project_duration_3,
            "project_github_3": project_github_3,
            "project_description_3": project_description_3,
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