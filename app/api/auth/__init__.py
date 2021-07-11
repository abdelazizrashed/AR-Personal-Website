from .controller import api
from .resources import (
    UserResource,
    UserLoginEmail,
    UserLoginUsername,
    UserRefresh,
    Users,
    UserLogout,
)


api.add_resource(UserResource, "/auth/user")
api.add_resource(UserLoginEmail, "/auth/login-email")
api.add_resource(UserLoginUsername, "/auth/login-username")
api.add_resource(UserRefresh, "/auth/refresh")
api.add_resource(Users, "/auth/users")
api.add_resource(UserLogout, "/auth/logout")
