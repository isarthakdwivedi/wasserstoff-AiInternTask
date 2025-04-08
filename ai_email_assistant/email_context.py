import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load API key
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


def understand_email_context(email_text):
    try:
        model = genai.GenerativeModel("models/gemini-1.5-pro")
        prompt = f"""
You are a smart email assistant. Analyze the following email and return a JSON response.

Email:
\"\"\"
{email_text}
\"\"\"

Return ONLY valid JSON in the following format, and nothing else:

{{
  "intent": "string",
  "action_items": ["string"],
  "suggested_reply": "string"
}}
"""
        response = model.generate_content(prompt)
        print("🔍 Gemini Raw Output:\n", response.text)
        return response.text.strip()
    except Exception as e:
        print(f"❌ Context Understanding Error: {e}")
        return None


# Optional: test it
if __name__ == "__main__":
    email = "Hey, checking in to discuss the next meeting. Are you free Thursday?"
    result = understand_email_context(email)
    print("Context:", result)
