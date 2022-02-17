import pyrebase
from flask import Flask
from typing import List
from .models import UserModel
from .interfaces import UserInterface
from random import randint
from app.api.shared.helpers.services import HelperServices


class UserServices:
    @staticmethod
    def json(user: UserModel) -> dict:
        if not user:  return None
        return {
            "userID": user.user_id,
            "username": user.username,
            "email": user.email,
        }

    @staticmethod
    def from_json(json: dict) -> UserModel:
        if not json: return
        attrs = dict(
            user_id=json.get("userID"),
            username=json.get("username"),
            email=json.get("email"),
            password=json.get("password"),
        )
        user = UserModel()
        return user.update(attrs)

    @staticmethod
    def retrieve_by_user_id(user_id: int, app: Flask) -> UserModel:
        db = HelperServices.get_firebase_database(app)
        results = db.child("Users").get()
        if not results.each: return None
        for result in results.each():
            if result.val().get("userID") == user_id:
                return UserServices.from_json(result.val())

        return None

    @staticmethod
    def retrieve_by_username(username: str, app: Flask) -> UserModel:
        db = HelperServices.get_firebase_database(app)
        results = db.child("Users").get()
        if  not results.each(): return None
        for result in results.each():
            if result.val().get("username") == username:
                return UserServices.from_json(result.val())

        return None

    @staticmethod
    def retrieve_by_email(email: str, app: Flask) -> UserModel:
        db = HelperServices.get_firebase_database(app)
        results = db.child("Users").get()
        if  not results.each(): return None
        for result in results.each():
            if result.val().get("email") == email:
                return UserServices.from_json(result.val())

        return None

    @staticmethod
    def retrieve_users(app: Flask) -> List[UserModel]:
        db = HelperServices.get_firebase_database(app)
        results = db.child("Users").get()
        users: List[UserModel] = []
        if not results.each(): return None
        for result in results.each():
            attrs = dict(result.val())
            user = UserServices.from_json(attrs)
            users.append(user)
        return users

    @staticmethod
    def create(attrs: dict, app: Flask) -> UserModel:
        db = HelperServices.get_firebase_database(app)
        if UserServices.retrieve_by_username(attrs.get("username"), app):
            return None
        if UserServices.retrieve_by_email(attrs.get("email"), app):
            return None
        user_id = UserServices.generate_user_id(app)
        attrs["userID"] = user_id
        attrs = db.child("Users").child(attrs.get("username")).set(dict(attrs))
        user = UserServices.from_json(attrs)
        return user

    @staticmethod
    def update(user: UserModel, updates: dict, app: Flask) -> UserModel:
        db = HelperServices.get_firebase_database(app)
        new_updates = {}
        if updates.get("username"):
            if UserServices.retrieve_by_username(updates.get("username"), app):
                return None
            new_updates["username"] = updates.get("username")
        else:
            new_updates["username"] = user.username
        if updates.get("email"):
            if UserServices.retrieve_by_username(updates.get("email"), app):
                return None
            new_updates["email"] = updates.get("email")
        else:
            new_updates["email"] = user.email
        if updates.get("password"):
            new_updates["password"] = updates.get("password")
        else:
            new_updates["password"] = user.password
        new_updates["userID"] = user.user_id
        db.child("Users").child(user.username).remove()
        attrs = (
            db.child("Users").child(new_updates.get("username")).set(dict(new_updates))
        )
        user_id = user.user_id
        user = UserServices.from_json(attrs)
        user.user_id = user_id
        return user

    @staticmethod
    def delete(user: UserModel, app: Flask) -> int:
        db = HelperServices.get_firebase_database(app)
        db.child("Users").child(user.username).remove()
        return user.user_id

    @staticmethod
    def generate_user_id(app: Flask) -> int:
        user_id = randint(0, 1000)
        user = UserServices.retrieve_by_user_id(user_id, app)
        if user != None:
            return UserServices.generate_user_id(app)
        return user_id
