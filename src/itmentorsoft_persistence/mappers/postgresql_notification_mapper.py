from itmentorsoft_persistence.dto.notificaction import Notification
from itmentorsoft_persistence.models.postgresql_notification_model import (
    NotificationEntity,
)


class NotificationMapper:
    @staticmethod
    def to_entity(notification: Notification) -> NotificationEntity:
        return NotificationEntity(
            id=notification.id,
            user_id=notification.user_id,
            subject=notification.subject,
            message=notification.message,
            read=notification.read,
            created_at=notification.created_at,
            updated_at=notification.updated_at,
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
