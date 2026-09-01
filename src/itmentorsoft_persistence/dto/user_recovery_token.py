import uuid


class RecoveryTokenInfo:
    """Data class to hold information about a recovery token.

    Args:
        user_id (str): The ID of the user associated with the recovery token.
        token (str): The generated recovery token.
        expiration_time (float): The expiration time of the token in seconds.
        status (str): The status of the token (default is "active").
    """

    def __init__(
        self, user_id: str, token: str, expiration_time: float, status: str = "active"
    ):
        self.user_id = user_id
        self.token = token
        self.expiration_time = expiration_time
        self.status = status
        self.id_trx = uuid.uuid4().hex


class UserRecoveryTokenResponse:
    def __init__(
        self, user_id: str, token_hashed: str, expiration_time: float, status: str
    ):
        self.user_id = user_id
        self.token_hashed = token_hashed
        self.expiration_time = expiration_time
        self.status = status