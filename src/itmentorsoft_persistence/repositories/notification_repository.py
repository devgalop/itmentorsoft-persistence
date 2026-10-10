from abc import ABC, abstractmethod

from itmentorsoft_persistence.dto.notificaction import (
    InsertNotificationRequest,
    Notification,
)


class NotificationRepository(ABC):

    @abstractmethod
    async def create_notification(self, notification: InsertNotificationRequest):
        """Create a new notification for a user.

        Args:
            notification (InsertNotificationRequest): The notification object to create.
        """
        pass

    @abstractmethod
    async def get_notifications_for_user(
        self, user_id: str
    ) -> list[Notification] | None:
        """Retrieve all notifications for a specific user.

        Args:
            user_id (str): The ID of the user to retrieve notifications for.

        Returns:
            list[Notification] | None: A list of notification objects for the user if any exist, otherwise None.
        """
        pass

    @abstractmethod
    async def get_notifications_unread_for_user(
        self, user_id: str
    ) -> list[Notification] | None:
        """Retrieve all unread notifications for a specific user.

        Args:
            user_id (str): The ID of the user to retrieve unread notifications for.

        Returns:
            list[Notification] | None: A list of unread notification objects for the user if any exist, otherwise None.
        """
        pass
