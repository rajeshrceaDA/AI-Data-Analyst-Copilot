def profile_to_resume_text(profile):
    """
    Convert Master Profile JSON into plain resume text
    for ATS Analysis.
    """

    sections = []

    # -------------------------
    # Basic Details
    # -------------------------

    sections.append(profile.get("name", ""))

    sections.append(profile.get("designation", ""))

    sections.append(profile.get("career_goal", ""))

    # -------------------------
    # Skills
    # -------------------------

    skills = profile.get("skills", [])

    if skills:

        sections.append("Skills")

        sections.append(" ".join(skills))

    # -------------------------
    # Experience
    # -------------------------

    sections.append(profile.get("job_title", ""))

    sections.append(profile.get("company_name", ""))

    sections.append(profile.get("responsibilities", ""))

    sections.append(profile.get("achievements", ""))

    # -------------------------
    # Education
    # -------------------------

    sections.append(profile.get("degree", ""))

    sections.append(profile.get("college", ""))

    # -------------------------
    # Projects
    # -------------------------

    sections.append(profile.get("projects", ""))

    # -------------------------
    # Certifications
    # -------------------------

    sections.append(profile.get("certifications", ""))

    # -------------------------
    # Languages
    # -------------------------

    sections.append(profile.get("languages", ""))

    return "\n".join(sections)