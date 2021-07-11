import pyrebase

from app.api.custom_blueprint import CustomBlueprint
from flask_restful import Api

services_blueprint = CustomBlueprint("services_blueprint", __name__)

firebase = None
storage = None
db = None


@services_blueprint.record
def record_params(setup_state):
    global firebase

    config = setup_state.app.config

    firebase_config = config.get("FIREBASE_CONFIG")

    # print(firebase_config)

    firebase = pyrebase.initialize_app(firebase_config)

    storage = firebase.storage()
    db = firebase.database()


api = Api(services_blueprint)