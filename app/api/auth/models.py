from .interfaces import UserInterface


class UserModel:

    user_id: int
    username: str
    email: str
    password: str

    def update(self, changes: UserInterface):
        for key, value in changes.items():
            setattr(self, key, value)
        return self