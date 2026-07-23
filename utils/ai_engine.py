import os
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI

# -----------------------------
# Load Environment Variables
# -----------------------------

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

if not OPENROUTER_API_KEY:
    raise Exception("OPENROUTER_API_KEY not found.")

# -----------------------------
# OpenRouter Client
# -----------------------------

client = OpenAI(
    api_key=OPENROUTER_API_KEY,
    base_url="https://openrouter.ai/api/v1"
)

# -----------------------------
# AI Function
# -----------------------------

def ask_ai(messages):

    response = client.chat.completions.create(

        model="deepseek/deepseek-v3.2",

        messages=messages,

        temperature=0.3,

        max_tokens=1200,

    )

    return response.choices[0].message.content