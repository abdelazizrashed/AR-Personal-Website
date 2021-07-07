import pyrebase
from flask import Blueprint, current_app
from flask_restful import Api

services_blueprint = Blueprint("services_blueprint", __name__)


api = Api(services_blueprint)

firebase = pyrebase.initialize_app(current_app.config["FIREBASE_CONFIG"])

storage = firebase.storage()
db = firebase.database()