import os
import sqlite3
from dotenv import load_dotenv
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Load environment variables
load_dotenv()

SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Get the script's directory
DB_PATH = os.path.join(BASE_DIR, "../emails.db")


def authenticate_gmail():
    """Authenticate with Gmail API and return service instance."""
    client_secret_file = os.getenv("CLIENT_SECRET_FILE")
    if not client_secret_file or not os.path.exists(client_secret_file):
        raise FileNotFoundError("❌ CLIENT_SECRET_FILE not found. Check .env file.")

    flow = InstalledAppFlow.from_client_secrets_file(client_secret_file, SCOPES)
    creds = flow.run_local_server(port=0)
    return build("gmail", "v1", credentials=creds)


def store_email(sender, recipient, subject, timestamp, body, thread_id):
    """Store an email in the SQLite database."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO emails (sender, recipient, subject, timestamp, body, thread_id) VALUES (?, ?, ?, ?, ?, ?)",
        (sender, recipient, subject, timestamp, body, thread_id)
    )

    conn.commit()
    conn.close()


def fetch_emails():
    """Fetch latest emails and store them in the database."""
    service = authenticate_gmail()
    results = service.users().messages().list(userId="me", maxResults=5).execute()
    messages = results.get("messages", [])

    if not messages:
        print("📭 No new emails found.")
        return

    for msg in messages:
        email_data = service.users().messages().get(userId="me", id=msg["id"]).execute()

        headers = email_data["payload"]["headers"]
        sender = next((h["value"] for h in headers if h["name"] == "From"), "Unknown")
        recipient = next((h["value"] for h in headers if h["name"] == "To"), "Unknown")
        subject = next((h["value"] for h in headers if h["name"] == "Subject"), "No Subject")
        timestamp = email_data.get("internalDate", "Unknown")
        body = email_data.get("snippet", "No Body")
        thread_id = email_data.get("threadId", "Unknown")

        # Store the email in the database
        store_email(sender, recipient, subject, timestamp, body, thread_id)
        print(f"✅ Stored email from {sender}: {subject}")


def fetch_latest_email():
    """Fetch the latest stored email from the database."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT sender, subject, body FROM emails ORDER BY timestamp DESC LIMIT 1;")
    email = cursor.fetchone()
    conn.close()

    if email:
        sender, subject, body = email
        return f"Sender: {sender}\nSubject: {subject}\n\n{body}"

    return None


if __name__ == "__main__":
    fetch_emails()
    latest_email = fetch_latest_email()
    if latest_email:
        print("\n📩 Latest Email:\n" + latest_email)
