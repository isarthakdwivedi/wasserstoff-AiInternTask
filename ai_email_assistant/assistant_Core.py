from ai_email_assistant.email_context import understand_email_context
from ai_email_assistant.web_search import search_with_serpapi
from ai_email_assistant.send_reply import send_auto_reply
from ai_email_assistant.calender_service import create_calendar_event
from ai_email_assistant.send_email import send_email
import os
from dotenv import load_dotenv
import json
import re

load_dotenv()
SENDER_EMAIL = os.getenv("EMAIL_ADDRESS")


def clean_json_response(response_text):
    return re.sub(r"^```(?:json)?|```$", "", response_text.strip(), flags=re.IGNORECASE).strip()


def handle_email(email_text):
    context_raw = understand_email_context(email_text)
    print("\n🔍 Gemini Raw Output:\n", context_raw)

    try:
        cleaned = clean_json_response(context_raw)
        context = json.loads(cleaned)
    except Exception as e:
        print("❌ Failed to parse LLM response:", e)
        return

    print("\n📥 Intent:", context.get("intent"))
    print("📝 Action Items:", context.get("action_items"))
    print("✉️ Suggested Reply:", context.get("suggested_reply"))

    full_reply = context.get("suggested_reply", "")

    if context.get("intent", "").lower() == "schedule meeting" or "schedule" in context.get("intent", "").lower():
        summary = "Project sync meeting"
        start_time = "2025-04-08T15:00:00"
        end_time = "2025-04-08T16:00:00"

        event_link = create_calendar_event(summary, start_time, end_time)
        full_reply += f"\n\n📅 I've scheduled the meeting here: {event_link}"

    elif context.get("intent", "").lower() in ["request for information", "question"]:
        search_query = context.get("action_items", [""])[0]
        results = search_with_serpapi(search_query)

        print("\n🔎 Web Results:")
        for r in results:
            print("-", r)

        summary_lines = "\n".join([f"- {r}" for r in results])
        full_reply += "\n\nHere’s what I found:\n" + summary_lines

    full_reply += f"\n\nRegards,\n{SENDER_EMAIL},\n Don't reply to this mail this is automated mail"

    print("\n✉️ Full Auto-Reply Draft:\n", full_reply)
    confirm = input("Send this email? (yes/no): ").strip().lower()

    if confirm == "yes":
        to_email = "@Senders_Email"
        subject = "APPLICATION FOR SOFTWARE DEVELOPER"
        send_email(to_email, subject, full_reply)
        print("✅ Email sent.")
    else:
        print("❌ Email not sent.")


if __name__ == "__main__":
    email = "Hey, I'm applying for AI intern role at your reputed organization please "
    handle_email(email)
