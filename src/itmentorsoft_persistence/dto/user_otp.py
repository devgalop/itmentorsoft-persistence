
from enum import Enum


class UserOTPRequest:
    def __init__(self, user_id: str, otp: str, expiration_time: float):
        self.user_id = user_id
        self.otp = otp
        self.expiration_time = expiration_time

class UserOTPStatus(Enum):
    PENDING = "pending"
    EXPIRED = "expired"

class UserOTP:
    def __init__(self, user_id: str, otp: str, status: str, expiration_time: float):
        self.user_id = user_id
        self.otp = otp
        self.status = status
        self.expiration_time = expiration_time
        
    