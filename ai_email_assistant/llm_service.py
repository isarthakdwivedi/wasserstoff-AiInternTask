import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Initialize the Gemini model
model = genai.GenerativeModel("models/gemini-1.5-pro")


def summarize_email(email_text):
    response = model.generate_content(f"Summarize this email concisely:\n\n{email_text}")
    return response.text


if __name__ == "__main__":
    email_text = "Hello, I hope you're doing well. I wanted to discuss our next meeting..."
    print(summarize_email(email_text))