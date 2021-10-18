from typing import List

from flask.app import Flask
from .models import YouTubeVidModel, DetailModel, ProjectModel
from app.api.shared.services import IMGInfoServices, PlatformServices, TechnologyServices



class YouTubeVidServices:

    @staticmethod 
    def json(vid: YouTubeVidModel) -> dict:
        return {
            "src": vid.src,
            "title": vid.title
        }

    @staticmethod
    def from_json(json: dict) -> YouTubeVidModel:
        vid = YouTubeVidModel()
        vid.src = json["src"]
        vid.title = json["title"]

        return vid


class DetailServices:

    @staticmethod
    def json(detail: DetailModel) -> dict:
        
        return {
            "name": detail.name,
            "description": detail.description
        }

    @staticmethod
    def from_json(json: dict) ->DetailModel:
        
        detail = DetailModel()

        detail.name = json["name"]
        detail.description = json["description"]

        return detail

class YouTubeVidsServices:

    @staticmethod 
    def json(vids: List[YouTubeVidModel]) -> dict:
        
        vids_lbl = "vids"

        return_dict = {vids_lbl: []}

        for vid in vids:
            return_dict[vids_lbl].append(YouTubeVidServices.json(vid))
        
        return return_dict

    @staticmethod
    def from_json(json: dict) -> List[YouTubeVidModel]:
        vids = []

        for vid_json in json["vids"]:
            vids.append(YouTubeVidServices.from_json(vid_json))

        return vids


class DetailsServices:

    @staticmethod
    def json(details: List[DetailModel]) -> dict:
        
        details_lbl = "details"

        json = {details_lbl: []}

        for detail in details:
            json[details_lbl].append(DetailServices.json(detail))

        return json

    @staticmethod
    def from_json(json: dict) ->List[DetailModel]:
        
        details = []

        for d_json in json["details"]:
            details.append(DetailServices.from_json(d_json))

        return details


class ProjectServices:

    # name: str
    # id_: str
    # platforms_ids: List[str]
    # technologies_ids: List[str]
    # img_url: str
    # description: str
    # github_url: str
    # app_store_url: str
    # google_play_store_url: str
    # website_url: str
    # youtube_vid: YouTubeVidModel
    # services_ids: List[str]
    # imgs: List[IMGInfoModel]
    # related_projects_ids: List[str]
    # detailed_services: List[DetailModel]
    # detailed_technologies: List[DetailModel]
    # detailed_platforms: List[DetailModel]

    @staticmethod 
    def json(project: ProjectModel, app: Flask) -> dict:
        json = dict()
        
        json["name"] = project.name
        json["id"] = project.id_
        json["platformsIds"] = project.platforms_ids
        json["technologiesIds"] = project.technologies_ids
        json["imgUrl"] = project.img_url
        json["description"] = project.description
        json["githubUrl"] = project.github_url
        json["appStoreUrl"] = project.app_store_url
        json["googlePlayStoreUrl"] = project.google_play_store_url
        json["websiteUrl"] = project.website_url
        json["youtubeVid"] = YouTubeVidServices.json(project.youtube_vid)
        json["servicesIds"] = project.services_ids
        json["imgs"] = [IMGInfoServices.json(img, app) for img in project.imgs]
        json["relatedProjectsIds"] = project.related_projects_ids
        json["detailedServices"] = DetailsServices.json(project.detailed_services)
        json["detailedTechnologies"] = DetailsServices.json(project.detailed_technologies)
        json["detailedPlatforms"] = DetailsServices.json(project.detailed_platforms)
        
        return json

    @staticmethod
    def json_partial(project: ProjectModel, app: Flask) -> dict:
        json = dict()
        json["name"] = project.name
        json["platforms"] = [PlatformServices.retrieve(id_, app).name for id_ in project.platforms_ids]
        json["technologies"] = [TechnologyServices.retrieve(id_, app).name for id_ in project.technologies_ids]

        json["imgURL"] = project.img_url
        json["id"] = project.id_

        return json

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