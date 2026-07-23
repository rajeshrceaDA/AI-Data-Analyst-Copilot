import os

from docx import Document
from pypdf import PdfReader


# ==========================================
# Read TXT
# ==========================================

def read_txt(file):

    return file.read().decode("utf-8")


# ==========================================
# Read DOCX
# ==========================================

def read_docx(file):

    document = Document(file)

    text = []

    for para in document.paragraphs:
        text.append(para.text)

    return "\n".join(text)


# ==========================================
# Read PDF
# ==========================================

def read_pdf(file):

    reader = PdfReader(file)

    text = []

    for page in reader.pages:

        page_text = page.extract_text()

        if page_text:
            text.append(page_text)

    return "\n".join(text)


# ==========================================
# Main Parser
# ==========================================

def parse_job_description(uploaded_file):

    if uploaded_file is None:
        return ""

    extension = os.path.splitext(uploaded_file.name)[1].lower()

    if extension == ".txt":
        return read_txt(uploaded_file)

    elif extension == ".docx":
        return read_docx(uploaded_file)

    elif extension == ".pdf":
        return read_pdf(uploaded_file)

    return ""