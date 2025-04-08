# 🤖 AI-Powered Email Assistant

## 📌 Overview
This project is an AI-powered personal email assistant that can:
- Read Gmail inbox
- Understand email context using Gemini 1.5 Pro
- Automatically generate and send replies
- Schedule calendar events
- Search the web using SerpAPI
- Notify users via Slack

## 🏗️ Architecture Diagram
```text
              ┌────────────────────┐
              │    Gmail Inbox     │
              └────────┬───────────┘
                       │
                       ▼
        ┌───────────────────────────┐
        │   Email Fetcher (Gmail)   │ ◄─── Auth via OAuth2 / App Password
        └───────────────────────────┘
                       │
                       ▼
        ┌───────────────────────────┐
        │ Parse + Store in SQLite   │
        └───────────────────────────┘
                       │
                       ▼
        ┌───────────────────────────┐
        │     Gemini 1.5 Pro        │ ◄─── Prompt for context (intent, reply)
        └───────────────────────────┘
                       │
                       ▼
    ┌────────────┬──────────────┬──────────────┐
    ▼            ▼              ▼              ▼
Reply Email   Web Search    Schedule Event   Slack Notify
   │         (SerpAPI)     (Google Calendar)     │
   ▼              ▼               ▼              ▼
SMTP/Gmail     Append to        Google       Slack API
               Email Body       Calendar
```

---

## 🛠️ Tools & Technologies Used
| Tool | Purpose |
|------|---------|
| **Gemini 1.5 Pro** | Understands email content & generates reply |
| **Gmail API / SMTP** | Email reading/sending |
| **Google Calendar API** | Event creation |
| **SerpAPI** | Web search for info requests |
| **Slack Web API** | Notifying users in Slack |
| **Python** | Core language |
| **SQLite** | Local email storage |
| **dotenv** | Secure environment config |

---

## 📩 Prompt Example (Gemini)
```python
prompt = f"""
You're a smart personal email assistant. Analyze the following email and extract:
1. Intent
2. Any action items
3. Suggested reply

Email:
"""
{email_text}
"""
Return response in JSON format:
{
  "intent": "...",
  "action_items": ["..."],
  "suggested_reply": "..."
}
"""
```

---

## 🔐 Security Practices
- `.env` file to store sensitive keys (Gemini, SerpAPI, SMTP)
- Gmail SMTP uses **App Password** for authentication
- Slack Bot Token stored securely
- No hard-coded credentials

---

## 🪛 Challenges & Solutions
| Issue | Solution |
|-------|----------|
| Gemini returned JSON with backticks | Used regex to clean and parse |
| SMTP failed with 534 error | Enabled 2FA + used App Password |
| Slack messages not sending | Added `chat:write` permission scope |

---

## 💡 AI Coding Assistant Usage
- **ChatGPT** was used extensively for:
  - Generating regex to clean JSON
  - Debugging SMTP, calendar, and parsing issues
  - Suggesting clean architecture and flow
  - Writing test prompts for LLM

---

## 🖼️ Optional Screenshots (Add if needed)
- ✅ Gmail inbox with new auto-reply
- ✅ Slack message with forwarded email
- ✅ Google Calendar with scheduled meeting

---

## 🔮 Future Improvements
- Store full email threads for context
- Smart threading with conversation memory
- Better LLM prompting using few-shot examples
- UI for managing emails and replies
- NLP-based intent classifier (fine-tuned model)

---

## 📁 Folder Structure
```bash
EmailAssistant/
├── ai_email_assistant/
│   ├── assistant_core.py
│   ├── email_context.py
│   ├── calender_service.py
│   ├── web_search.py
│   ├── send_email.py
│   └── send_reply.py
├── .env
├── requirements.txt
└── README.md
```

---

## ✅ Final Checklist
- [x] Gmail API/SMTP integrated
- [x] LLM parsing + reply generation
- [x] Calendar scheduling
- [x] Web search via SerpAPI
- [x] Slack notifications
- [ ] SQLite email storage ❗(in progress)
- [x] Prompt engineering & LLM formatting
- [x] Email confirmation before sending

