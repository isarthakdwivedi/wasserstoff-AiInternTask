import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))  # use the correct key name


def summarize_email(email_text):
    try:
        model = genai.GenerativeModel("models/gemini-1.5-pro")
        response = model.generate_content(
            f"Summarize the following email in a concise manner:\n\n{email_text}"
        )
        return response.text
    except Exception as e:
        print(f"❌ LLM Error: {e}")
        return "Summary not available due to error."


if __name__ == "__main__":
    test_email = "Hey, just a quick update on the project. We've completed phase one and will start testing tomorrow."
    try:
        summary = summarize_email(test_email)
        print("Summary:", summary)
    except Exception as e:
        print("❌ LLM Error:", e)


