from abc import ABC, abstractmethod

from itmentorsoft_persistence.dto.assign_role import (
    AssignRoleToUserCommand,
)
from itmentorsoft_persistence.dto.user import (
    CompleteUserResponse,
    User,
    UserResponse,
)
from itmentorsoft_persistence.dto.user_access import UserAccessTries
from itmentorsoft_persistence.dto.user_otp import UserOTP, UserOTPRequest


class UserRepository(ABC):
    """Interface for user repository implementations.

    Args:
        ABC (ABC): Abstract base class for user repository implementations.
    """

    @abstractmethod
    async def get_user_by_username(self, username: str) -> CompleteUserResponse | None:
        """Search user by username field.

        Args:
            username (str): The username of the user to search for.

        Returns:
            CompleteUserResponse: The complete user response object if found, otherwise None.
        """
        pass

    @abstractmethod
    async def get_user_by_email(self, email: str) -> CompleteUserResponse | None:
        """Search user by email.

        Args:
            email (str): The email of the user to search for.

        Returns:
            CompleteUserResponse: The complete user response object if found, otherwise None.
        """
        pass

    @abstractmethod
    async def get_user_response_by_email(self, email: str) -> UserResponse | None:
        """Search user by email.

        Args:
            email (str): The email of the user to search for.

        Returns:
            UserResponse: The user response object if found, otherwise None.
        """
        pass

    @abstractmethod
    async def get_user_by_id(self, user_id: str) -> UserResponse | None:
        """Search user by ID.

        Args:
            user_id (str): The ID of the user to search for.

        Returns:
            UserResponse: The user response object if found, otherwise None.
        """
        pass

    @abstractmethod
    async def save(self, user: User):
        """Save changes into database

        Args:
            user (User): The user object to be saved or updated in the database.
        """
        pass

    @abstractmethod
    async def change_password(self, user_id: str, new_password_hashed: str):
        """Change the password of a user.

        Args:
            user_id (str): The ID of the user whose password is to be changed.
            new_password_hashed (str): The new hashed password to be set for the user.
        """
        pass

    @abstractmethod
    async def assign_role_to_user(self, request: AssignRoleToUserCommand):
        """ "Assign a role to a user.

        Args:
            request (AssignRoleToUserCommand): The request object containing user ID and role information.

        """
        pass

    @abstractmethod
    async def get_available_roles(self) -> list[str]:
        """Get the list of available roles.

        Returns:
            list[str]: A list of available roles in the system.
        """
        pass

    @abstractmethod
    async def get_admin_users(self) -> list[UserResponse]:
        """Get the list of admin users.

        Returns:
            list[UserResponse]: A list of user response objects for admin users.
        """
        pass

    @abstractmethod
    async def get_users_by_role(self, role: str) -> list[UserResponse]:
        """Get the list of users by role.

        Args:
            role (str): The role to filter users by.

        Returns:
            list[UserResponse]: A list of users with the specified role.
        """
        pass

    @abstractmethod
    async def update_user_status(self, user_id: str, new_status: str):
        """Update the status of a user.

        Args:
            user_id (str): The ID of the user whose status is to be updated.
            new_status (str): The new status to be set for the user.
        """
        pass

    @abstractmethod
    async def update_username(self, user_id: str, new_username: str, name: str):
        """Update the username of a user.

        Args:
            user_id (str): The ID of the user whose username is to be updated.
            new_username (str): The new username to be set for the user.
            name (str): The new name to be set for the user.
        """
        pass
    
    @abstractmethod
    async def get_user_otp(self, user_id: str) -> UserOTP | None:
        """Get the OTP details for a user.

        Args:
            user_id (str): The ID of the user to search for.

        Returns:
            UserOTP: The user OTP object if found, otherwise None.
        """
        pass
    
    @abstractmethod
    async def save_user_otp(self, user_otp: UserOTPRequest):
        """Save the OTP details for a user.

        Args:
            user_otp (UserOTPRequest): The user OTP request object to be saved in the database.

        """
        pass
    
    @abstractmethod
    async def get_login_try_counter(self, user_id: str) -> UserAccessTries:
        """Get the login try counter for a user.

        Args:
            user_id (str): The ID of the user to search for.

        Returns:
            UserAccessTries: The user access tries object containing the number of login attempts, block time, and blocked status for the user.
        """
        pass

    @abstractmethod
    async def increment_login_try_counter(self, user_id: str, increment: int = 1, should_block: bool = False):
        """Increment the login try counter for a user.

        Args:
            user_id (str): The ID of the user whose login try counter is to be incremented.
            increment (int, optional): The amount by which to increment the login try counter. Defaults to 1.
            should_block (bool, optional): Whether the user should be blocked if the counter exceeds the limit. Defaults to False.

        """
        pass
    
    @abstractmethod
    async def reset_login_try_counter(self, user_id: str):
        """Reset the login try counter for a user.

        Args:
            user_id (str): The ID of the user whose login try counter is to be reset.

        """
        pass
