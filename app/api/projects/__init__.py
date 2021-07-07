import pyrebase
from flask import Blueprint, current_app

projects_blueprint = Blueprint("projects_blueprint", __name__)

firebase = pyrebase.initialize_app(current_app.config["FIREBASE_CONFIG"])

storage = firebase.storage()
db = firebase.database()