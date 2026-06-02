from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

from spam_rules import classify_email
from label_helper import get_or_create_label

import os

SCOPES = [
    "https://www.googleapis.com/auth/gmail.modify"
]


def get_gmail_service():

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

    return build(
        "gmail",
        "v1",
        credentials=creds
    )


def scan_emails():

    service = get_gmail_service()

    spam_label = get_or_create_label(
        service,
        "AI-Spam"
    )

    newsletter_label = get_or_create_label(
        service,
        "AI-Newsletter"
    )

    important_label = get_or_create_label(
        service,
        "AI-Important"
    )

    results = service.users().messages().list(
        userId="me",
        maxResults=20
    ).execute()

    messages = results.get(
        "messages",
        []
    )

    spam_count = 0
    newsletter_count = 0
    important_count = 0

    email_rows = []

    for msg in messages:

        detail = service.users().messages().get(
            userId="me",
            id=msg["id"]
        ).execute()

        headers = detail["payload"]["headers"]

        subject = "(無主旨)"
        sender = ""

        for h in headers:

            if h["name"] == "Subject":
                subject = h["value"]

            if h["name"] == "From":
                sender = h["value"]

        result = classify_email(subject)

        if result == "spam":

            spam_count += 1

            service.users().messages().modify(
                userId="me",
                id=msg["id"],
                body={
                    "addLabelIds": [spam_label]
                }
            ).execute()

        elif result == "newsletter":

            newsletter_count += 1

            service.users().messages().modify(
                userId="me",
                id=msg["id"],
                body={
                    "addLabelIds": [newsletter_label]
                }
            ).execute()

        else:

            important_count += 1

            service.users().messages().modify(
                userId="me",
                id=msg["id"],
                body={
                    "addLabelIds": [important_label]
                }
            ).execute()

        email_rows.append(
            {
                "Sender": sender,
                "Category": result,
                "Subject": subject
            }
        )

    return {
        "spam_count": spam_count,
        "newsletter_count": newsletter_count,
        "important_count": important_count,
        "emails": email_rows
    }
