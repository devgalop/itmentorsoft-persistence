from datetime import datetime


class InsertNotificationRequest:
    def __init__(
        self, user_id: str, subject: str, message: str, url: str | None = None
    ):
        self.user_id = user_id
        self.subject = subject
        self.message = message
        self.url = url


class Notification:
    def __init__(
        self,
        id: int,
        user_id: str,
        subject: str,
        message: str,
        created_at: datetime,
        updated_at: datetime,
        read: bool = False,
        url: str | None = None,
    ):
        self.id = id
        self.user_id = user_id
        self.subject = subject
        self.message = message
        self.read = read
        self.created_at = created_at
        self.updated_at = updated_at
        self.url = url
