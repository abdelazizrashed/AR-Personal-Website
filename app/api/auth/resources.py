from flask import current_app as app
from flask_restful import Resource, reqparse
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    jwt_required,
    get_jwt_identity,
    get_jwt,
)
from .interfaces import UserInterface
from .models import UserModel
from .services import UserServices
from datetime import datetime, timezone
from app.api.shared.jwt.models import TokenBlocklistModel
from app.api.shared.db_man.services import db
from werkzeug.security import safe_str_cmp


_user_parser = reqparse.RequestParser()

_user_parser.add_argument("username", type=str, help="User username.")

_user_parser.add_argument("email", type=str, help="User email.")

_user_parser.add_argument("password", type=str, help="User password.")

_user_parser.add_argument("userID", type=int, help="User id.")


class UserResource(Resource):
    @jwt_required(fresh=True)
    def post(self):
        data = _user_parser.parse_args()
        try:
            if not data.get("username"):
                return {
                    "description": "username is required",
                    "error ": "not_found",
                }, 404
            if not data.get("email"):
                return {"description": "email is required", "error ": "not_found"}, 404
            if UserServices.retrieve_by_email(data.get("email"), app):
                return {
                    "description": "A user with this email already exists.",
                    "error": "email_exists",
                }, 400
            if UserServices.retrieve_by_username(data.get("username"), app):
                return {
                    "description": "A user with this username already exists.",
                    "error": "username_exists",
                }, 400

            user = UserServices.create(dict(data), app)

            if not user:
                return {
                    "description": "email or username already exists",
                    "error": "email_username_exists",
                }, 400
            access_token = create_access_token(user.user_id, fresh=True)
            refresh_token = create_refresh_token(user.user_id)
            return {
                "message": "User created successfully.",
                "user": UserServices.json(user),
                "accessToken": access_token,
                "refreshToken": refresh_token,
            }, 201
        except:
            return {
                "description": "Internal server error",
                "error": "internal_server_error",
            }, 500

    @jwt_required(fresh=True)
    def put(self):
        claims = get_jwt()
        data = _user_parser.parse_args()
        try:
            if not data.get("userID"):
                return {
                    "description": "userID is required to update user data",
                    "error": "missing_ifno",
                }, 400

            user: UserModel = UserServices.retrieve_by_user_id(data.get("userID"), app)

            if not user:
                user = UserServices.create(dict(data), app)
                if not user:
                    return {
                        "description": "email or username already exists",
                        "error": "email_username_exists",
                    }, 400
                return {
                    "message": "User data created successfully",
                    "user_data": UserServices.json(user),
                }

            updates: UserModelInterface = dict()

            if data.get("username"):
                if data.get("username") != claims.get("username"):
                    if UserServices.retrieve_by_username(data["username"], app):
                        return {
                            "description": "A user with this username already exists",
                            "error": "username_exists",
                        }, 400

                    updates["username"] = data["username"]
            if data["password"]:
                if data["password"] != user.password:
                    updates["password"] = data["password"]
                else:
                    return {
                        "description": "Your new password can't be the same as your old one",
                        "error": "invalid_password",
                    }, 400

            if data["email"]:
                if data["email"] != user.email:
                    if UserServices.retrieve_by_email(data["email"], app):
                        return {
                            "description": "A user with this email already exists",
                            "error": "email_exists",
                        }, 400
                    updates["email"] = data["email"]

            if len(updates) == 0:
                return {
                    "description": "No new data was provided",
                    "error": "no_info",
                }, 404

            new_user: UserModel = UserServices.update(user, updates, app)

            return {
                "message": "User data updated successfully",
                "user_data": UserServices.json(new_user),
            }
        except:
            return {
                "description": "Internal server error",
                "error": "internal_server_error",
            }, 500

    @jwt_required(fresh=True)
    def get(self):
        claims = get_jwt()
        data = _user_parser.parse_args()

        try:
            if data["userID"]:
                user = UserServices.retrieve_by_user_id(data["userID"], app)
                if not user:
                    return {
                        "description": "The userID is incorrect or the user doesn't exists",
                        "error": "invalid_user_id",
                    }, 400
                return {"user_info": UserServices.json(user)}, 200
            if data["username"]:
                user = UserServices.retrieve_by_username(data["username"], app)
                if user:
                    return {"user_info": UserServices.json(user)}, 200
                else:
                    return {
                        "description": "The username is incorrect or the user doesn't exist",
                        "error": "invalid_username",
                    }, 404
            if data["email"]:
                user = UserServices.retrieve_by_email(data["email"], app)
                if user:
                    return {"user_info": UserServices.json(user)}, 200
                else:
                    return {
                        "description": "The email is incorrect or the user doesn't exist",
                        "error": "invalid_email",
                    }, 404
            return {
                "description": "No user info was supplied. Please make sure to send the userID, username, or email.",
                "error": "no_info",
            }, 400
        except:
            return {
                "description": "Internal server error",
                "error": "internal_server_error",
            }, 500

    @jwt_required(fresh=True)
    def delete(self):
        claims = get_jwt()
        data = _user_parser.parse_args()

        try:
            user: UserModel = UserServices.retrieve_by_user_id(data["userID"], app)
            Helpers.logout(claims.get("jti"))
            if not UserServices.delete(user, app):
                return {
                    "message": "User couldn't be deleted. The user may not exist"
                }, 404
            return {"message": "User deleted successfully."}, 200
        except:
            return {
                "description": "Internal server error",
                "error": "internal_server_error",
            }, 500


class UserLoginEmail(Resource):
    def post(self):
        data = _user_parser.parse_args()

        try:
            user: UserModel = UserServices.retrieve_by_email(data["email"], app)

            if not user:
                return {
                    "description": "The email is incorrect or the user doesn't exist",
                    "error": "invalid_email",
                }, 404

            return Helpers.login(user, data["password"])
        except:
            return {
                "description": "Internal server error",
                "error": "internal_server_error",
            }, 500


class UserLoginUsername(Resource):
    def post(self):
        data = _user_parser.parse_args()

        try:
            user: UserModel = UserServices.retrieve_by_username(data["username"], app)

            if not user:
                return {
                    "description": "The username is incorrect or the user doesn't exist",
                    "error": "invalid_username",
                }, 404

            return Helpers.login(user, data["password"])
        except:
            return {
                "description": "Internal server error",
                "error": "internal_server_error",
            }, 500


class UserLogout(Resource):
    @jwt_required()
    def delete(self):
        try:
            jti = get_jwt()["jti"]
            return Helpers.logout(jti)
        except:
            return {
                "description": "Internal server error",
                "error": "internal_server_error",
            }, 500


class UserRefresh(Resource):
    @jwt_required(refresh=True)
    def post(self):
        try:
            current_user = get_jwt_identity()
            new_token = create_access_token(identity=current_user, fresh=False)
            return {"accessToken": new_token}, 200
        except:
            return {
                "description": "Internal server error",
                "error": "internal_server_error",
            }, 500


class Users(Resource):
    @jwt_required(fresh=True)
    def get(self):
        try:
            claims = get_jwt()
            users: List[UserModel] = UserServices.retrieve_users(app)
            return {"users": [UserServices.json(user) for user in users]}
        except:
            return {
                "description": "Internal server error",
                "error": "internal_server_error",
            }, 500


class Helpers:
    @staticmethod
    def login(user: UserModel, password):
        if safe_str_cmp(user.password, password):
            access_token = create_access_token(identity=user.user_id, fresh=True)
            refresh_token = create_refresh_token(identity=user.user_id)

            return {"accessToken": access_token, "refreshToken": refresh_token}, 200
        return {
            "description": "The password provided didn't match the user password.",
            "error": "invalid_password",
        }, 401

    @staticmethod
    def logout(jti):
        now = datetime.now(timezone.utc)
        db.session.add(TokenBlocklistModel(jti=jti, created_at=now))
        db.session.commit()
        return {"message": "User logged out."}, 200
