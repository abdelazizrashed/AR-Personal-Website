import pyrebase
from flask import Blueprint, current_app
from flask_restful import Api
from .resources import InfoResource

info_blueprint = Blueprint("info_blueprint", __name__)

api = Api(info_blueprint)

firebase = pyrebase.initialize_app(current_app.config["FIREBASE_CONFIG"])

storage = firebase.storage()
db = firebase.database()

# Todo: add flask restfule resources
api.add_resource(InfoResource, "/info")
