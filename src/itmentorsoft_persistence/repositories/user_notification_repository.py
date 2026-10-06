from abc import ABC, abstractmethod

from itmentorsoft_persistence.dto.user import UserResponse


class UserNotificationRepository(ABC):
    @abstractmethod
    async def get_user_by_id(self, user_id: str) -> UserResponse | None:
        """Search user by ID.

        Args:
            user_id (str): The ID of the user to search for.

        Returns:
            UserResponse: The user response object if found, otherwise None.
        """
        pass
