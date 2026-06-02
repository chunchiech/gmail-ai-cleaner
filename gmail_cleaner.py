from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

from spam_rules import classify_email

import os

SCOPES = [
    "https://www.googleapis.com/auth/gmail.readonly"
]

creds = None

if os.path.exists("token.json"):
    creds = Credentials.from_authorized_user_file(
        "token.json",
        SCOPES
    )

if not creds or not creds.valid:

    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())

    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            "credentials.json",
            SCOPES
        )

        creds = flow.run_local_server(port=0)

    with open("token.json", "w") as token:
        token.write(creds.to_json())

service = build(
    "gmail",
    "v1",
    credentials=creds
)

results = service.users().messages().list(
    userId="me",
    maxResults=20
).execute()

messages = results.get("messages", [])

spam_count = 0
newsletter_count = 0
important_count = 0

print("\n===== Gmail AI Cleaner =====\n")

for msg in messages:

    detail = service.users().messages().get(
        userId="me",
        id=msg["id"]
    ).execute()

    headers = detail["payload"]["headers"]

    subject = "(無主旨)"

    for h in headers:
        if h["name"] == "Subject":
            subject = h["value"]
            break

    result = classify_email(subject)

    if result == "spam":
        spam_count += 1
        icon = "🚫"

    elif result == "newsletter":
        newsletter_count += 1
        icon = "📰"

    else:
        important_count += 1
        icon = "✅"

    print(
        f"{icon} [{result.upper():10}] {subject}"
    )

print("\n============================")
print("📊 Summary")
print("============================")
print(f"🚫 Spam       : {spam_count}")
print(f"📰 Newsletter : {newsletter_count}")
print(f"✅ Important  : {important_count}")
print("============================\n")
