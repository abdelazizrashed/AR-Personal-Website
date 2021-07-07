import pyrebase
from flask import Blueprint, current_app

certificates_blueprint = Blueprint("certificates_blueprint", __name__)

firebase = pyrebase.initialize_app(current_app.config["FIREBASE_CONFIG"])

storage = firebase.storage()
db = firebase.database()