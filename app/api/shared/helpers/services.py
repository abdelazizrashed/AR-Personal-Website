import pyrebase
from flask import Flask


class HelperServices:
    @staticmethod
    def get_url_from_cloud_path(cloud_path: str, firebase_storage):
        if cloud_path:
            return firebase_storage.child(cloud_path).get_url(None)
        return None

    @staticmethod
    def get_firebase_object(app: Flask) -> pyrebase.pyrebase.Firebase:
        return pyrebase.initialize_app(app.config["FIREBASE_CONFIG"])

    @staticmethod
    def get_firebase_database(app: Flask) -> pyrebase.pyrebase.Database:
        firebase = HelperServices.get_firebase_object(app)
        return firebase.database()

    @staticmethod
    def get_firebase_storage(app: Flask) -> pyrebase.pyrebase.Storage:
        firebase = HelperServices.get_firebase_object(app)
        return firebase.storage()
