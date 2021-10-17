from typing import List

from flask.app import Flask
from .models import YouTubeVidModel, DetailModel, ProjectModel



class YouTubeVidServices:

    @staticmethod 
    def json(vid: YouTubeVidModel) -> dict:
        raise NotImplementedError

    @staticmethod
    def from_json(json: dict) -> YouTubeVidModel:
        raise NotImplementedError


class DetailServices:

    @staticmethod
    def json(detail: DetailModel) -> dict:
        
        raise NotImplementedError

    @staticmethod
    def from_json(json: dict) ->DetailModel:
        raise NotImplementedError


class YouTubeVidsServices:

    @staticmethod 
    def json(vids: List[YouTubeVidModel]) -> dict:
        raise NotImplementedError

    @staticmethod
    def from_json(json: dict) -> List[YouTubeVidModel]:
        raise NotImplementedError


class DetailsServices:

    @staticmethod
    def json(details: List[DetailModel]) -> dict:
        
        raise NotImplementedError

    @staticmethod
    def from_json(json: dict) ->List[DetailModel]:
        raise NotImplementedError


class ProjectServices:

    @staticmethod 
    def json(project: ProjectModel) -> dict:
        raise NotImplementedError

    @staticmethod
    def json_partial(project: ProjectModel) -> dict:
        raise NotImplementedError

    @staticmethod
    def from_json(json: dict) -> ProjectModel:
        raise NotImplementedError

    #CRUD methods
    @staticmethod
    def create(attr: dict, app: Flask) -> ProjectModel:
        raise NotImplementedError

    @staticmethod
    def retrieve(id: dict, app: Flask) -> ProjectModel:
        raise NotImplementedError

    @staticmethod
    def update(updates: dict, app: Flask) -> ProjectModel:
        raise NotImplementedError

    @staticmethod
    def delete(id: str, app: Flask) -> str:
        raise NotImplementedError


class ProjectsServices:

    @staticmethod 
    def json(projects: List[ProjectModel]) -> dict:
        raise NotImplementedError

    @staticmethod
    def json_partial(projects: List[ProjectModel]) -> dict:
        raise NotImplementedError

    @staticmethod
    def from_json(json: dict) -> List[ProjectModel]:
        raise NotImplementedError

    #CRUD methods
    @staticmethod
    def create(attr: dict, app: Flask) -> List[ProjectModel]:
        raise NotImplementedError

    @staticmethod
    def retrieve(app: Flask, ids: List[str] = None, service_id: str = None, platform_id: str = None, technology_id: str = None) -> List[ProjectModel]:
        raise NotImplementedError

    @staticmethod
    def update(updates: dict, app: Flask) -> List[ProjectModel]:
        raise NotImplementedError

    @staticmethod
    def delete(ids: List[str], app: Flask) -> List[str]:
        raise NotImplementedError