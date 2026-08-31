class AssignRoleToUserCommand:
    def __init__(self, user_id: str, role_id: str):
        self.user_id = user_id
        self.role_id = role_id
