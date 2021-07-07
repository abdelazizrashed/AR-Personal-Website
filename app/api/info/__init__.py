import pyrebase
from flask import Blueprint

info_blueprint = Blueprint("info_blueprint", __name__)

firebase = pyrebase.initialize_app()