from flask import current_app as app
from flask_restful import Resource, reqparse, request
from flask_jwt_extended import jwt_required

from app.api.shared.helpers.services import HelperServices
from .services import IMGInfoServices, TechnologiesServices, TechnologyServices, PlatformServices, PlatformsServices


_tech_parser = reqparse.RequestParser()
_tech_parser.add_argument("name", type=str, help="Name of the technology")
_tech_parser.add_argument("description", type=str, help="Description of the technology")
_tech_parser.add_argument("id", type=str, help="The id of the technology as saved in the database, you can get it from making a get request to /shared/technologies")


_platform_parser = reqparse.RequestParser()
_platform_parser.add_argument("name", type=str, help="Name of the platform")
_platform_parser.add_argument("description", type=str, help="Description of the platform")
_platform_parser.add_argument("id", type=str, help="The id of the platform as saved in the database, you can get it from making a get request to /shared/platforms")



class TechnologiesResource(Resource):

    @jwt_required()
    def post(self):
        #Todo: Check if you can make this request work
        return{
            "description": "You are not allowed to create multiple technologies at once. Create them one by one",
            "error": "invalid_operation"
        }, 409

    @jwt_required()
    def put(self):
        data = request.get_json()
        techs = TechnologiesServices.update(data, app)
        return{
            "technologies": TechnologiesServices.json_all(techs)
        }, 200

    @jwt_required()
    def delete(self):
        ids = request.args.getlist("id")
        if not ids or len(ids) == 0:
            return {
                "description": "You should include a list of technologies id's to delete",
                "error": "missing_info"
            }, 400
        res = TechnologiesServices.delete(ids, app)
        return res

    def get(self):
        ids = request
        ids = request.args.getlist("id")
        partial = request.args.get("partial", type=bool)
        techs = TechnologiesServices.retrieve(app, ids=ids)
        if partial:
            return TechnologiesServices.json_partial(techs), 200
        else: 
            return TechnologiesServices.json_all(techs), 200
        


class TechnologyResource(Resource):

    @jwt_required()
    def post(self):
        data = _tech_parser.parse_args()
        technology = TechnologyServices.create(data, app)
        return TechnologyServices.json_all(technology), 200

    @jwt_required()
    def put(self):
        id_ = request.args.get("id", type=str)
        data = _tech_parser.parse_args()
        technology = TechnologyServices.update(data, id_, app)
        return TechnologyServices.json_all(technology), 200

    @jwt_required()
    def delete(self):
        id_ = request.args.get("id", type=str)
        status_code = TechnologyServices.delete(id_, app)
        if status_code == 200:
            return{
                "message": "Succeeded",
                "id": id_
            }, 200
        else:
            return {
                "message": "Failed",
                "id": id_
            }, status_code

    def get(self):
        id_ = request.args.get("id", type=str)
        partial = request.args.get("partial", type=bool)
        tech = TechnologyServices.retrieve(id_, app)
        if partial:
            return TechnologyServices.json_partial(tech), 200

        else:
            return TechnologyServices.json_all(tech), 200


class PlatformsResource(Resource):

    @jwt_required()
    def post(self):
        #Todo: Check if you can make this request work
        return{
            "description": "You are not allowed to create multiple technologies at once. Create them one by one",
            "error": "invalid_operation"
        }, 409

    @jwt_required()
    def put(self):
        data = request.get_json()
        platforms = PlatformsServices.update(data, app)
        return{
            "platforms": PlatformsServices.json_all(platforms)
        }, 200

    @jwt_required()
    def delete(self):
        ids = request.args.getlist("id")
        if not ids or len(ids) == 0:
            return {
                "description": "You should include a list of platforms' id's to delete",
                "error": "missing_info"
            }, 400
        res = PlatformsServices.delete(ids, app)
        return res

    def get(self):
        ids = request
        ids = request.args.getlist("id")
        partial = request.args.get("partial", type=bool)
        platforms = PlatformsServices.retrieve(app, ids=ids)
        if partial:
            return PlatformsServices.json_partial(platforms), 200
        else: 
            return PlatformsServices.json_all(platforms), 200


class PlatformResource(Resource):

    @jwt_required()
    def post(self):
        data = _platform_parser.parse_args()
        platform = PlatformServices.create(data, app)
        return PlatformServices.json_all(platform), 200

    @jwt_required()
    def put(self):
        id_ = request.args.get("id", type=str)
        data = _platform_parser.parse_args()
        platform = PlatformServices.update(data, id_, app)
        return PlatformServices.json_all(platform), 200

    @jwt_required()
    def delete(self):
        id_ = request.args.get("id", type=str)
        status_code = PlatformServices.delete(id_, app)
        if status_code == 200:
            return{
                "message": "Deleted platform object successfully",
                "id": id_
            }, 200
        else:
            return {
                "message": "Failed",
                "id": id_
            }, status_code

    def get(self):
        id_ = request.args.get("id", type=str)
        partial = request.args.get("partial", type=bool)
        platform = PlatformServices.retrieve(id_, app)
        if partial:
            return PlatformServices.json_partial(platform), 200
        else:
            return PlatformServices.json_all(platform), 200


class ImageResource(Resource):

    _img_parser = reqparse.RequestParser()
    _img_parser.add_argument("cloudPath")

    @jwt_required()
    def post(self):
        files, datas = HelperServices.seperate_files_and_json_data(request, files_keys=["img"])
        cloud_path = HelperServices.upload_file(files["img"][0], app)
        return {
            "cloudPath": cloud_path
        }, 200


    def get(self):
        data = self._img_parser.parse_args()
        if not data.get("cloudPath"):
            return {
                "description": "cloudPath is required",
                "error": "not_found"
            }, 404
        storage = HelperServices.get_firebase_storage(app)
        url = HelperServices.get_url_from_cloud_path(data.get("cloudPath"), storage)

        return {
            "url": url
        }, 200

    # @jwt_required()
    # def put(self):
    #     pass

    @jwt_required()
    def delete(self):
        data = self._img_parser.parse_args()
        if not data.get("cloudPath"):
            return {
                "description": "cloudPath is required",
                "error": "not_found"
            }, 404
        cloud_path = HelperServices.delete_file(data.get("cloudPath"), app)
        return {
            "cloudPath": cloud_path
        }, 200
        