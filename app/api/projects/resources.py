from flask import current_app as app
from flask_restful import Resource, reqparse, request
from flask_jwt_extended import jwt_required

from typing import List

from .services import ProjectServices, ProjectsServices


_project_parser = reqparse.RequestParser()
_project_parser.add_argument("name", type=str)
_project_parser.add_argument("id", type=str)
_project_parser.add_argument("platformsIds", type=List[str])
_project_parser.add_argument("technologiesIds", type=List[str])
_project_parser.add_argument("imgUrl", type=str)
_project_parser.add_argument("description", type=str)
_project_parser.add_argument("githubUrl", type=str)
_project_parser.add_argument("appStoreUrl", type=str)
_project_parser.add_argument("googlePlayStoreUrl", type=str)
_project_parser.add_argument("websiteUrl", type=str)
_project_parser.add_argument("youtubeVid", type=dict)
_project_parser.add_argument("servicesIds", type=List[str])
_project_parser.add_argument("imgs", type=List[dict])
_project_parser.add_argument("relatedProjectsIds", type=List[str])
_project_parser.add_argument("detailedServices", type=List[dict])
_project_parser.add_argument("detailedTechnologies", type=List[dict])
_project_parser.add_argument("detailedPlatforms", type=List[dict])


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

    @jwt_required()
    def post(self):
        data = _project_parser.parse_args()

        project = ProjectServices.create(data, app)

        if not project:
            return {
                "description": "Faced unknown error while creating the project",
                "error": "unknown_error"
            }, 520
        return ProjectServices.json(project), 201

    @jwt_required()
    def put(self):
        data = _project_parser.parse_args()

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
        return {
            "id": del_id
        }, 200


class ProjectsResources(Resource):
    
    def get(self):
        raise NotImplementedError

    @jwt_required()
    def post(self):
        raise NotImplementedError

    @jwt_required()
    def put(self):
        raise NotImplementedError

    @jwt_required()
    def delete(self):
        raise NotImplementedError
