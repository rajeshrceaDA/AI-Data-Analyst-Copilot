import os
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI

# Root folder
BASE_DIR = Path(__file__).resolve().parent.parent

# Load .env
load_dotenv(BASE_DIR / ".env")

# Read API Key
api_key = os.getenv("OPENROUTER_API_KEY")

print("API Key Loaded:", api_key[:15] + "..." if api_key else "Not Found")

# Create OpenRouter Client
client = OpenAI(
    api_key=api_key,
    base_url="https://openrouter.ai/api/v1"
)

def ask_ai(prompt):

    response = client.chat.completions.create(
        model="openrouter/free",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content