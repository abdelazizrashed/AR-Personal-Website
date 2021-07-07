import pyrebase
from flask import Blueprint, current_app
from flask_restful import Api

info_blueprint = Blueprint("info_blueprint", __name__)

api = Api(info_blueprint)

firebase = pyrebase.initialize_app(current_app.config["FIREBASE_CONFIG"])

storage = firebase.storage()
db = firebase.database()