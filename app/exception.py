class UserNotFound(Exception):
    def __int__(self, user_id):
        self.user_id = user_id
