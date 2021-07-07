import pyrebase
from flask import Blueprint, current_app

auth_blueprint = Blueprint("auth_blueprint", __name__)

from flask_restful import Api

api = Api(auth_blueprint)

firebase = pyrebase.initialize_app(current_app.config["FIREBASE_CONFIG"])

storage = firebase.storage()
db = firebase.database()