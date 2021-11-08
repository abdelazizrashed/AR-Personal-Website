from flask import current_app as app
from flask_jwt_extended.view_decorators import jwt_required
from flask_restful import Resource, reqparse, request
# from werkzeug.wrappers import request

from app.api.services.services import ServiceServices
from app.api.shared.helpers.services import HelperServices


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
        data = _service_parser.parse_args()
        
        if not data.get("logo") or not data.get("logo").get("cloudPath"):
            return {
                "description": "The logo of the service is required as well as it's cloudPath",
                "error": "missing_info"
            }, 400
        
        if not HelperServices.check_if_file_exists(data.get("logo").get("cloudPath"), app):
            return {
                "description": "Image not found in the database. Please upload the image first using the url /shared/image, then attach the resulting cloudPath to the request.",
                "error": "not_found"
            }, 404

        service = ServiceServices.create(data, app)
        if not service:
            return {
                "description": "Faced unknown error while creating the service",
                "error": "unknown_error"
            }, 520
        return ServiceServices.json(service, app), 201

    def get(self):
        id_ = request.args.get("id", type=str)
        partial = request.args.get("partial", type=bool)
        service = ServiceServices.retreive(id_, app)
        if not service:
            return {
                "description": f"Service with id:<{id_}> couldn't be found",
                "error": "not_found"
            }, 404
        return ServiceServices.json_partial(service, app), 200 if partial else ServiceServices.json(service, app)


    @jwt_required()
    def put(self):
        id_ = request.args.get("id", type=str)
        data = _service_parser.parse_args()
        
        if data.get("logo") and not data.get("logo").get("cloudPath"):
            return {
                "description": "If you are going to update the logo you need to upload the new logo to the database via /shared/image post request then add the cloudPath to the logo",
                "error": "missing_info"
            }, 400
        
        if not HelperServices.check_if_file_exists(data.get("logo").get("cloudPath"), app):
            return {
                "description": "Image not found in the database. Please upload the image first using the url /shared/image, then attach the resulting cloudPath to the request.",
                "error": "not_found"
            }, 404
        service = ServiceServices.update(data, id_, app)
        return ServiceServices.json(service, app), 204


    @jwt_required()
    def delete(self):
        id_ = request.args.get("id", type=str)

        return ServiceServices.delete(id_, app)


class ServicesResources(Resource):

    @jwt_required()
    def post(self):
        #Todo: Check if you can make this request work
        return{
            "description": "You are not allowed to create multiple projects at once. Create them one by one",
            "error": "invalid_operation"
        }, 409

    def get(self):
        ids = request.args.getlist("id", type=str)
        partial = request.args.get("partial", type=bool)

    @jwt_required()
    def put(self):
        pass

    @jwt_required()
    def delete(self):
        pass

