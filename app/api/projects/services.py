from typing import List
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
    def json(detail: List[DetailModel]) -> dict:
        
        raise NotImplementedError

    @staticmethod
    def from_json(json: dict) ->List[DetailModel]:
        raise NotImplementedError


class ProjectServices:

    pass


class ProjectsServices:

    pass