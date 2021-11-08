from flask import current_app as app #request
from flask_restful import Resource, reqparse, request
from flask_jwt_extended import jwt_required

from typing import List

from app.api.shared.helpers.services import HelperServices

from .services import ProjectServices, ProjectsServices



# def img_parser(location: tuple=())-> reqparse.RequestParser:
#     parser = reqparse.RequestParser()
#     parser.add_argument("alt", type= str, location=location)
#     parser.add_argument("caption", type=str, location=location)
#     parser.add_argument("cloudPath", type=str, location=location)
#     return parser


_project_parser = reqparse.RequestParser()
_project_parser.add_argument("name", type=str)
_project_parser.add_argument("id", type=str)
_project_parser.add_argument("platformsIds", type=str, action="append")
_project_parser.add_argument("technologiesIds", type=str, action="append")
_project_parser.add_argument("img", type=dict)
# _img_parser = img_parser(("img",))
_project_parser.add_argument("description", type=str)
_project_parser.add_argument("githubUrl", type=str)
_project_parser.add_argument("appStoreUrl", type=str)
_project_parser.add_argument("googlePlayStoreUrl", type=str)
_project_parser.add_argument("websiteUrl", type=str)
_project_parser.add_argument("youtubeVid", type=dict)
_project_parser.add_argument("servicesIds", type=str, action="append")
_project_parser.add_argument("imgs", type=dict, action="append")
# _imgs_parser = img_parser(("imgs",))
_project_parser.add_argument("relatedProjectsIds", type=str, action="append")
_project_parser.add_argument("detailedServices", type=dict, action="append")
_project_parser.add_argument("detailedTechnologies", type=dict, action="append")
_project_parser.add_argument("detailedPlatforms", type=dict, action="append")

# def parse_child(child: reqparse.RequestParser, root_args: dict)-> dict:
#     return child.parse_args(req=root_args)


class ProjectResources(Resource):
    
    def get(self):
        id_ = request.args.get("id", type=str)
        partial = request.args.get("partial", type=bool)
        project = ProjectServices.retrieve(id_, app)
        if not project:
            return {
                "description": f"Project with id:<{id_}> couldn't be found",
                "error": "not_found"
            }, 404
        return ProjectServices.json(project), 200 if not partial else ProjectServices.json_partial(project), 200

    def post(self):
        data = _project_parser.parse_args()
        if not HelperServices.check_if_file_exists(data.get("img").get("cloudPath"), app):
            return {
                "description": "Image not found in the database. Please upload the image first using the url /shared/image, then attach the resulting cloudPath to the request.",
                "error": "not_found"
            }, 404
        for img in data.get("imgs"):
            if not HelperServices.check_if_file_exists(img.get("cloudPath"), app):
                return {
                    "description": "Image not found in the database. Please upload the image first using the url /shared/image, then attach the resulting cloudPath to the request.",
                    "error": "not_found"
                }, 404
        project = ProjectServices.create(data, app)

        if not project:
            return {
                "description": "Faced unknown error while creating the project",
                "error": "unknown_error"
            }, 520
        return ProjectServices.json(project), 201

    @jwt_required()
    def put(self):
        #*Data Validation
        data = _project_parser.parse_args()
        if data.get("img") and data.get("img").get("cloud_path") and not HelperServices.check_if_file_exists(data.get("img").get("cloudPath"), app):
            return {
                "description": "Image not found in the database. Please upload the image first using the url /shared/image, then attach the resulting cloudPath to the request.",
                "error": "not_found"
            }, 404
        if data.get("imgs"):
            if isinstance(data.get("imgs"), list):
                for img in data.get("imgs"):
                    if not HelperServices.check_if_file_exists(img.get("cloudPath"), app):
                        return {
                            "description": "Image not found in the database. Please upload the image first using the url /shared/image, then attach the resulting cloudPath to the request.",
                            "error": "not_found"
                        }, 404
            elif HelperServices.check_if_file_exists(data.get("imgs").get("cloudPath"), app):
                return {
                    "description": "Image not found in the database. Please upload the image first using the url /shared/image, then attach the resulting cloudPath to the request.",
                    "error": "not_found"
                }, 404

        project = ProjectServices.update(data, app)

        if not project:
            return {
                "description": "Faced unknown error while updating the project",
                "error": "unknown_error"
            }, 520
        return ProjectServices.json(project), 200

    @jwt_required()
    def delete(self):
        id_ = request.args.get("id", type=str)

        del_id = ProjectServices.delete(id_, app)

        if not del_id:
            return {
                "description": "Faced unknown error while deleting the project",
                "error": "unknown_error"
            }, 520
        return 200


class ProjectsResources(Resource):
    
    def get(self):
        ids = request.args.getlist("id")
        partial = request.args.get("partial", type=bool)
        service = request.args.get("service", type=str)
        platform = request.args.get("platform", type=str)
        technology = request.args.get("technology", type=str)

        projects = ProjectsServices.retrieve(app, ids, service, platform, technology)

        return ProjectsServices.json_partial(projects), 200 if partial else ProjectsServices.json(projects), 200

    @jwt_required()
    def post(self):
        #Todo: Check if you can make this request work
        return{
            "description": "You are not allowed to create multiple technologies at once. Create them one by one",
            "error": "invalid_operation"
        }, 409

    @jwt_required()
    def put(self):
        data = _project_parser.parse_args()

        projects = ProjectsServices.update(data, app)

        return ProjectsServices.json(projects), 200

    @jwt_required()
    def delete(self):
        ids = request.args.getlist("id")

        ids = ProjectsServices.delete(ids, app)

        return 200