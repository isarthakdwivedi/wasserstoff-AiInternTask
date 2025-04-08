import sqlite3
from ai_email_assistant.gpt_summarizer import summarize_email


def process_emails():
    # Correct database path
    conn = sqlite3.connect("ai_email_assistant/emails.db")
    cursor = conn.cursor()

    # Check if the table exists before querying
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='emails';")
    if not cursor.fetchone():
        print("❌ Error: Table 'emails' does not exist. Run setup_db.py first.")
        return

    cursor.execute("SELECT id, sender, subject, body FROM emails WHERE summary IS NULL")
    emails = cursor.fetchall()

    for email in emails:
        email_id, sender, subject, body = email
        email_text = f"Sender: {sender}\nSubject: {subject}\n\n{body}"

        summary = summarize_email(email_text)

        cursor.execute("UPDATE emails SET summary = ? WHERE id = ?", (summary, email_id))

    conn.commit()
    conn.close()
    print("✔️ Emails processed with LLM.")


if __name__ == "__main__":
    process_emails()
