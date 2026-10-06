from datetime import datetime


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
    ):
        self.id = id
        self.user_id = user_id
        self.subject = subject
        self.message = message
        self.read = read
        self.created_at = created_at
        self.updated_at = updated_at
