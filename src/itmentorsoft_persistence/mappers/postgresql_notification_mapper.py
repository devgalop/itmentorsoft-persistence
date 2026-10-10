from datetime import datetime

from itmentorsoft_persistence.dto.notificaction import (
    Notification,
    InsertNotificationRequest,
)
from itmentorsoft_persistence.models.postgresql_notification_model import (
    NotificationEntity,
)


class NotificationMapper:
    @staticmethod
    def to_entity(notification: InsertNotificationRequest) -> NotificationEntity:
        return NotificationEntity(
            user_id=notification.user_id,
            subject=notification.subject,
            message=notification.message,
            read=False,
            created_at=datetime.now(),
            updated_at=datetime.now(),
        )

    @staticmethod
    def to_dto(entity: NotificationEntity) -> Notification:
        return Notification(
            id=entity.id,
            user_id=entity.user_id,
            subject=entity.subject,
            message=entity.message,
            read=entity.read,
            created_at=entity.created_at,
            updated_at=entity.updated_at,
        )
