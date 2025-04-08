import sqlite3

# Connect to the correct database path
conn = sqlite3.connect("ai_email_assistant/emails.db")
cursor = conn.cursor()

# Create the emails table with all necessary fields
cursor.execute('''
    CREATE TABLE IF NOT EXISTS emails (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        sender TEXT NOT NULL,
        recipient TEXT,
        subject TEXT NOT NULL,
        timestamp TEXT,
        body TEXT NOT NULL,
        thread_id TEXT,
        summary TEXT
    )
''')

conn.commit()
conn.close()
print("✔️ Database initialized.")
