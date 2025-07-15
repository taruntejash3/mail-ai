import os
from dotenv import load_dotenv
import google.generativeai as genai
# Load your API key from .env
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY not found. Please set it in your .env file.")
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-2.0-flash")
def compose_email_with_gemini(scenario: str, language: str) -> str:
    prompt = f"Write a complete email in {language} for the following scenario:\n\n{scenario.strip()}"
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"⚠️ Gemini Error: {str(e)}"
def reply_email_with_gemini(received_email: str, language: str) -> str:
    prompt = f"Reply in {language} to the following email:\n\n{received_email.strip()}"
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"⚠️ Gemini Error: {str(e)}"

