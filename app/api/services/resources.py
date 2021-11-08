from flask import current_app as app
from flask_jwt_extended.view_decorators import jwt_required
from flask_restful import Resource, reqparse


_service_parser = reqparse.RequestParser()
_service_parser.add_argument("id", type=str)
_service_parser.add_argument("name", type=str)
_service_parser.add_argument("description", type=str)
_service_parser.add_argument("projectsIds", type=str, action="append")
_service_parser.add_argument("otherServicesIds", type=str, action="append")

_service_parser.add_argument("content", type=dict, action="append")
_service_parser.add_argument("technologies", type=dict, action="append")


class ServiceResources(Resource):

    @jwt_required()
    def post(self):
        pass

    def get(self):
        pass

    @jwt_required()
    def put(self):
        pass

    @jwt_required()
    def delete(self):
        pass


class ServicesResources(Resource):

    @jwt_required()
    def post(self):
        pass

    def get(self):
        pass

    @jwt_required()
    def put(self):
        pass

    @jwt_required()
    def delete(self):
        pass

