from abc import ABC, abstractmethod
import uuid

from itmentorsoft_persistence.dto.user_recovery_token import RecoveryTokenInfo, UserRecoveryTokenResponse





class UserRecoveryTokenRepository(ABC):
    """Interface for user recovery token repository implementations.

    Args:
        ABC (ABC): Abstract base class for user recovery token repository implementations.
    """

    @abstractmethod
    async def save_token(self, recovery_token_info: RecoveryTokenInfo):
        """Save the generated token along with the associated user ID and expiration time.

        Args:
            recovery_token_info (RecoveryTokenInfo): The information about the recovery token.
        """
        pass

    @abstractmethod
    async def get_user_id_by_transaction_id(
        self, transaction_id: str
    ) -> UserRecoveryTokenResponse | None:
        """Retrieve the user recovery token response associated with a given transaction ID.

        Args:
            transaction_id (str): The transaction ID to search for.

        Returns:
            UserRecoveryTokenResponse: The user recovery token response associated with the transaction ID if found, otherwise None.
        """
        pass

    @abstractmethod
    async def revoke_tokens_by_user_id(self, user_id: str):
        """Revoke all recovery tokens associated with a given user ID.

        Args:
            user_id (str): The ID of the user whose tokens should be revoked.
        """
        pass
