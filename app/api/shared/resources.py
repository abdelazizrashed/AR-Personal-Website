from flask import current_app as app
from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required


class TechnologiesResource(Resource):

    @jwt_required()
    def post(self):
        raise NotImplementedError

    @jwt_required()
    def put(self):
        raise NotImplementedError

    @jwt_required()
    def delete(self):
        raise NotImplementedError

    def get(self):
        raise NotImplementedError


class TechnologyResource(Resource):

    @jwt_required()
    def post(self):
        raise NotImplementedError

    @jwt_required()
    def put(self):
        raise NotImplementedError

    @jwt_required()
    def delete(self):
        raise NotImplementedError

    def get(self):
        raise NotImplementedError


class PlatformsResource(Resource):

    @jwt_required()
    def post(self):
        raise NotImplementedError

    @jwt_required()
    def put(self):
        raise NotImplementedError

    @jwt_required()
    def delete(self):
        raise NotImplementedError

    def get(self):
        raise NotImplementedError


class PlatformResource(Resource):

    @jwt_required()
    def post(self):
        raise NotImplementedError

    @jwt_required()
    def put(self):
        raise NotImplementedError

    @jwt_required()
    def delete(self):
        raise NotImplementedError

    def get(self):
        raise NotImplementedError
