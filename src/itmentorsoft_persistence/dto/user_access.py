
class UserAccessTries:
    def __init__(self, 
                 user_id: str, 
                 retry_count: int,
                 block_time: int,
                 is_blocked: bool):
        self.user_id = user_id
        self.retry_count = retry_count
        self.block_time = block_time
        self.is_blocked = is_blocked