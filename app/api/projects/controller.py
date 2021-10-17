import pyrebase

from app.api.custom_blueprint import CustomBlueprint
from flask_restful import Api

projects_blueprint = CustomBlueprint("projects_blueprint", __name__)

api = Api(projects_blueprint)