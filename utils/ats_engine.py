import re
from utils.skills_database import SKILLS

# ==========================================
# Stop Words
# ==========================================

STOP_WORDS = {
    "a", "an", "and", "the", "to", "of", "for",
    "with", "in", "on", "at", "is", "are",
    "be", "as", "or", "by", "from", "this",
    "that", "it", "its", "into", "your",
    "our", "their", "will", "can", "should"
}

def clean_text(text):
    """
    Convert text to lowercase and remove special characters.
    """

    if not text:
        return ""

    text = text.lower()

    text = re.sub(r"[^a-z0-9\s]", " ", text)

    text = re.sub(r"\s+", " ", text)

    return text.strip()


def extract_keywords(text):
    """
    Extract useful keywords by removing stop words.
    """

    cleaned = clean_text(text)

    words = cleaned.split()

    keywords = {
        word
        for word in words
        if word not in STOP_WORDS and len(word) > 2
    }

    return keywords

# ==========================================
# Extract Skills
# ==========================================

def extract_skills(text):
    """
    Extract only predefined professional skills
    from the resume or job description.
    """

    cleaned = clean_text(text)

    found_skills = set()

    for skill in SKILLS:

        if skill.lower() in cleaned:

            found_skills.add(skill)

    return found_skills

def calculate_ats_score(resume_text, jd_text):

    resume_text = clean_text(resume_text)

    jd_text = clean_text(jd_text)
    """
    Compare Resume and Job Description keywords.
    """

    resume_keywords = extract_skills(resume_text)

    jd_keywords = extract_skills(jd_text)

    if len(jd_keywords) == 0:
        return {
            "score": 0,
            "matched": [],
            "missing": [],
            "total_keywords": 0
        }

    matched = sorted(list(resume_keywords.intersection(jd_keywords)))

    missing = sorted(list(jd_keywords - resume_keywords))

    score = round((len(matched) / len(jd_keywords)) * 100)

    return {
        "score": score,
        "matched": matched,
        "missing": missing,
        "total_keywords": len(jd_keywords)
    }