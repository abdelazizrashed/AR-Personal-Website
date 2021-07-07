import pyrebase
from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager


def create_app():

    app = Flask(__name__)
    app.config.from_pyfile('/config/dev.config')
    app.config.from_envvar('APPLICATION_CONFIG_FILE')

    api = Api(app)

    jwt = JWTManager(app)

    firebase = pyrebase.initialize_app(app.config["FIREBASE_CONFIG"])
    storage = firebase.storage()
    db = firebase.database()

    return app