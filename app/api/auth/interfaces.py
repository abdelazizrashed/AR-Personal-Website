from mypy_extensions import TypedDict


class UserInterface(TypedDict, total=False):

    user_id: int
    username: str
    email: str
    password: str