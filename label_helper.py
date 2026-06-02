def get_or_create_label(service, label_name):

    labels = service.users().labels().list(
        userId="me"
    ).execute()

    for label in labels["labels"]:
        if label["name"] == label_name:
            return label["id"]

    label_object = {
        "name": label_name,
        "labelListVisibility": "labelShow",
        "messageListVisibility": "show"
    }

    created_label = service.users().labels().create(
        userId="me",
        body=label_object
    ).execute()

    return created_label["id"]
