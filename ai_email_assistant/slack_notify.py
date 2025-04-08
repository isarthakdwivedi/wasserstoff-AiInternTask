import os
import requests
from dotenv import load_dotenv

load_dotenv()


def send_slack_message(message, channel="#all-assistant"):
    token = os.getenv("SLACK_BOT_TOKEN")
    res = requests.post(
        "https://slack.com/api/chat.postMessage",
        headers={"Authorization": f"Bearer {token}"},
        data={"channel": channel, "text": message}
    )
    print(res.json())


# Example usage
if __name__ == "__main__":
    send_slack_message("📬 New important email received!", "#all-assistant")
