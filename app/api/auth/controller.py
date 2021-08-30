import pyrebase

from app.api.custom_blueprint import CustomBlueprint
from flask_restful import Api

#Create the module blueprint
auth_blueprint = CustomBlueprint("auth_blueprint", __name__)

#Important data used across the module to store/ retrieve data
firebase = None
storage = None
db = None

#Assigning the data from the config that is attached to blueprint at creation
@auth_blueprint.record
def record_params(setup_state):
    global firebase

    config = setup_state.app.config

    firebase_config = config.get("FIREBASE_CONFIG")

    # print(firebase_config)

    firebase = pyrebase.initialize_app(firebase_config)

    storage = firebase.storage()
    db = firebase.database()


#Initialize the api object from flask_restful using the created blueprint
api = Api(auth_blueprint)