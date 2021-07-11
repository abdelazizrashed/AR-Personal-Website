import pyrebase

from app.api.custom_blueprint import CustomBlueprint
from flask_restful import Api

certificates_blueprint = CustomBlueprint("certificates_blueprint", __name__)

firebase = None
storage = None
db = None


@certificates_blueprint.record
def record_params(setup_state):
    global firebase

    config = setup_state.app.config

    firebase_config = config.get("FIREBASE_CONFIG")

    # print(firebase_config)

    firebase = pyrebase.initialize_app(firebase_config)

    storage = firebase.storage()
    db = firebase.database()


api = Api(certificates_blueprint)