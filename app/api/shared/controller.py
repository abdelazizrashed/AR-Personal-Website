from app.api.custom_blueprint import CustomBlueprint
from flask_restful import Api

shared_blueprint = CustomBlueprint("shared_blueprint", __name__)


api = Api(shared_blueprint)