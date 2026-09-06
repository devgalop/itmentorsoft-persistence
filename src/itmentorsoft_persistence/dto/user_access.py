
class IncrementLoginTryCounterRequest:
    def __init__(self, 
                 user_id: str, 
                 counter: int,
                 is_temporarily_blocked: bool,
                 temporary_block_expiration: float,
                 is_definitively_blocked: bool):
        self.user_id = user_id
        self.counter = counter
        self.is_temporarily_blocked = is_temporarily_blocked
        self.temporary_block_expiration = temporary_block_expiration
        self.is_definitively_blocked = is_definitively_blocked

class UserAccessTries:
    def __init__(self, 
                 user_id: str, 
                 retry_count: int,
                 is_temporarily_blocked: bool,
                 temporary_block_expiration: float,
                 definitively_blocked: bool):
        self.user_id = user_id
        self.retry_count = retry_count
        self.temporary_block_expiration = temporary_block_expiration
        self.is_temporarily_blocked = is_temporarily_blocked
        self.definitively_blocked = definitively_blocked