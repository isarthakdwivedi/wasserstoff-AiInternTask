from ai_email_assistant.Scripts.authenticate_gmail import fetch_latest_email
from ai_email_assistant.Scripts.authenticate_gmail import store_email
from ai_email_assistant.assistant_Core import handle_email


def run_email_assistant():
    print("📬 Fetching latest email...")
    email_text = fetch_latest_email()

    if not email_text:
        print("⚠️ No new emails found.")
        return

    print("\n📥 Processing email:\n", email_text)
    handle_email(email_text)


if __name__ == "__main__":
    run_email_assistant()
