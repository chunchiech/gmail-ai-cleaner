from gmail_cleaner import get_gmail_service


def clean_spam():

    service = get_gmail_service()

    labels = service.users().labels().list(
        userId="me"
    ).execute()

    spam_label_id = None

    for label in labels["labels"]:

        if label["name"] == "AI-Spam":
            spam_label_id = label["id"]
            break

    if not spam_label_id:
        return 0

    messages = service.users().messages().list(
        userId="me",
        labelIds=[spam_label_id]
    ).execute()

    count = 0

    for msg in messages.get(
        "messages",
        []
    ):

        service.users().messages().trash(
            userId="me",
            id=msg["id"]
        ).execute()

        count += 1

    return count


def archive_newsletters():

    service = get_gmail_service()

    labels = service.users().labels().list(
        userId="me"
    ).execute()

    newsletter_label_id = None

    for label in labels["labels"]:

        if label["name"] == "AI-Newsletter":
            newsletter_label_id = label["id"]
            break

    if not newsletter_label_id:
        return 0

    messages = service.users().messages().list(
        userId="me",
        labelIds=[newsletter_label_id]
    ).execute()

    count = 0

    for msg in messages.get(
        "messages",
        []
    ):

        service.users().messages().modify(
            userId="me",
            id=msg["id"],
            body={
                "removeLabelIds": [
                    "INBOX"
                ]
            }
        ).execute()

        count += 1

    return count
