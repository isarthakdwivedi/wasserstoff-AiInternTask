# 📬 AI-Powered Email Assistant – Documentation

## 🧠 Objective
To build an AI-based email assistant that can:
- Fetch and analyze emails.
- Understand intent using an LLM (Gemini 1.5 Pro).
- Auto-generate or suggest replies.
- Schedule meetings via Google Calendar.
- Perform web searches.
- Notify via Slack.
- Maintain safeguards (confirmation before email sending).

---

## 🧱 Architecture Overview

```
              +---------------------+
              |  Gmail API / IMAP   |
              +----------+----------+
                         |
                         v
                +-----------------+
                | Email Fetcher   |
                +--------+--------+
                         |
                         v
      +----------------> SQLite DB <----------------+
      |                  (Storage)                  |
      |                                             |
+-----v----+                                 +------v------+
| Gemini   |                                 | Slack Bot   |
| 1.5 Pro  |                                 +-------------+
+--+-------+                                         |
   |                                                 v
   |       +----------------------------+     +------v------+
   +-----> | Context Understanding +    +---> | Web Search  |
           | Prompted Reply Drafting    |     | (SerpAPI)   |
           +-------------+--------------+     +------+------+
                         |                          |
                         v                          |
               +---------v---------+                |
               | Action Execution  |<---------------+
               | (Reply / Calendar / Slack)         |
               +-------------------+
```

---

## 🛠️ Tools & Libraries Used

| Tool/Library         | Purpose                                      |
|----------------------|----------------------------------------------|
| **Google Gemini 1.5 Pro** | Understand email content & generate replies |
| **Gmail API**        | Email fetching and SMTP sending              |
| **SerpAPI**          | Perform web search for user questions        |
| **Google Calendar API** | Schedule meetings                          |
| **Slack Web API**    | Notify about important emails                |
| **SQLite**           | Store emails with metadata                   |
| **Python**           | Backend scripting                            |
| **dotenv**           | Securely manage credentials                  |

---

## 💬 Prompt Example (LLM)

```python
prompt = f"""
You're a smart personal email assistant. Analyze the following email and extract:

1. Intent (e.g., meeting request, update, question)
2. Any action items
3. Suggested reply

Email:
\"\"\"
{email_text}
\"\"\"
Return response in this JSON format:

{
  "intent": "...",
  "action_items": ["..."],
  "suggested_reply": "..."
}
"""
```

---

## 🔐 Security Practices

- Used **environment variables** via `.env` to store:
  - Gemini API Key
  - Gmail App Password
  - SerpAPI Key
  - Slack Bot Token

- Used **App-Specific Password** for Gmail SMTP (2FA enforced).
- Avoided logging sensitive data like full email content or passwords.

---

## 🛠️ Bugs/Challenges & How They Were Solved

| Issue | Resolution |
|-------|------------|
| **Gemini LLM JSON parsing failed due to backticks** | Used regex to clean Markdown ```json formatting |
| **SMTP Error 534 (App password required)** | Generated app-specific password & updated credentials |
| **Parsing multi-line responses** | Stripped unnecessary formatting & ensured JSON compatibility |
| **Conditional auto-sending logic** | Added input confirmation prompt before sending |

---

## 🧠 How ChatGPT Helped (AI Coding Assistant Usage)

- Suggested architecture & tools (Gemini vs OpenAI).
- Helped write Gmail + Calendar + Slack integration code.
- Diagnosed JSON formatting bugs from LLM output.
- Generated Python regex for response cleaning.
- Proposed full reply-drafting logic with safeguards.
- Created database schema and explained threading.
- Provided sample prompts and web search integration logic.

**Conclusion**: ChatGPT accelerated development by ~60-70% by providing real-time coding help, architecture suggestions, and troubleshooting guidance.

---


## 🖼️ Optional Screenshots to Include
- Gmail inbox with automated replies.
- Google Calendar showing scheduled event.
- Slack message received from assistant.

---

📄 Generated on 2025-04-06 13:05:51
