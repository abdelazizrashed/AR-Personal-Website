from typing import List

from flask.app import Flask
from werkzeug.exceptions import NotFound
from .models import YouTubeVidModel, DetailModel, ProjectModel
from app.api.shared.services import IMGInfoServices, PlatformServices, TechnologyServices
from app.api.shared.helpers.services import HelperServices


#Todo: Images upload is faulted as well as technologies and platforms have a second look on how you would change it. I commented them so you won't forget

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

    @staticmethod 
    def json(project: ProjectModel, app: Flask) -> dict:
        json = dict()
        
        json["name"] = project.name
        json["id"] = project.id_
        json["platforms"] = [PlatformServices.retrieve(id_, app).name for id_ in project.platforms_ids]
        json["technologies"] = [TechnologyServices.retrieve(id_, app).name for id_ in project.technologies_ids]
        storage = HelperServices.get_firebase_storage(app)
        json["img"] = IMGInfoServices.json(project.img)
        # HelperServices.get_url_from_cloud_path(project.img_cloud_path, storage)
        json["description"] = project.description
        json["githubUrl"] = project.github_url
        json["appStoreUrl"] = project.app_store_url
        json["googlePlayStoreUrl"] = project.google_play_store_url
        json["websiteUrl"] = project.website_url
        json["youtubeVid"] = YouTubeVidServices.json(project.youtube_vid)
        json["servicesIds"] = project.services_ids
        json["imgs"] = [IMGInfoServices.json(img, app) for img in project.imgs]
        json["relatedProjects"] = ProjectsServices.json_partial(ProjectsServices.retrieve(app, ids = project.related_projects_ids)) 
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

        storage = HelperServices.get_firebase_storage(app)
        json["img"] = IMGInfoServices.json(project.img)
        # HelperServices.get_url_from_cloud_path(project.img_cloud_path, storage)
        json["id"] = project.id_
        return json

    @staticmethod
    def from_json(json: dict) -> ProjectModel:
        project = ProjectModel()
        project.name =json["name"] 
        project.id_ =json["id"]
        project.related_projects_ids =json["platformsIds"]
        project.technologies_ids =json["technologiesIds"] 
        project.img =IMGInfoServices.from_json(json.get("img"))
        project.description =json["description"] 
        project.github_url =json["githubUrl"] 
        project.app_store_url =json["appStoreUrl"]
        project.google_play_store_url =json["googlePlayStoreUrl"] 
        project.website_url =json["websiteUrl"] 
        project.youtube_vid =YouTubeVidServices.from_json(json["youtubeVid"])
        project.services_ids =json["servicesIds"] 
        
        project.imgs =[IMGInfoServices.from_json(img_json) for img_json in json["imgs"]]
        project.related_projects_ids =json["relatedProjectsIds"]
        project.detailed_services =[DetailServices.from_json(j) for j in json["detailedServices"]]
        project.detailed_technologies =[DetailServices.from_json(j) for j in json["detailedTechnologies"]]
        project.detailed_platforms =[DetailServices.from_json(j) for j in json["detailedPlatforms"]]

        return project



    #*CRUD methods
    @staticmethod
    def create(attr: dict, app: Flask) -> ProjectModel:
        db = HelperServices.get_firebase_database(app)
        id_ = db.child("projects").push(attr)["name"]
        attr["id"] = id_
        project = ProjectServices.from_json(attr)
        return project

    @staticmethod
    def retrieve(id_: dict, app: Flask) -> ProjectModel:
        db = HelperServices.get_firebase_database(app)
        attrs = db.child("projects").child(id_).get()
        if attrs == None:
            return None
        return ProjectServices.from_json(attrs)

    @staticmethod
    def update(updates: dict, id_: str, app: Flask) -> ProjectModel:
        db = HelperServices.get_firebase_database(app)
        attrs = db.child("projects").child(id_).update(updates)
        if attrs == None:
            return None
        attrs["id"] = id_
        return ProjectServices.from_json(attrs)

    @staticmethod
    def delete(id_: str, app: Flask) -> int:
        db = HelperServices.get_firebase_database(app)
        res = db.child("projects").child(id_).remove()
        return res.status_code


class ProjectsServices:

    @staticmethod 
    def json(projects: List[ProjectModel], app: Flask) -> dict:
        return {"projects": [ProjectServices.json(project, app) for project in projects]}


    @staticmethod
    def json_partial(projects: List[ProjectModel], app: Flask) -> dict:
        return {"projects": [ProjectServices.json_partial(project, app) for project in projects]}

    @staticmethod
    def from_json(json: dict) -> List[ProjectModel]:
        return [ProjectServices.from_json(p_json) for p_json in json["projects"]]

    #CRUD methods
    @staticmethod
    def create(attr: dict, app: Flask) -> List[ProjectModel]:
        return [ProjectServices.create(p_attrs, app) for p_attrs in attr["projects"]]

    @staticmethod
    def retrieve(app: Flask, ids: List[str] = None, service_id: str = None, platform_id: str = None, technology_id: str = None) -> List[ProjectModel]:
        projects: List[ProjectModel] = []
        db = HelperServices.get_firebase_database(app)
        attrs: dict = db.child("projects").get()
        for key, value in attrs.items():
            p_attrs = value
            p_attrs["id"] = key
            projects.append(ProjectServices.from_json(p_attrs))
        for project in projects:
            if ids and not project.id_ in ids:
                #id filter
                projects.remove(project)
            if service_id and not service_id in project.services_ids:
                #service filter
                projects.remove(project)
            if platform_id and not platform_id in project.platforms_ids:
                #platform filter
                projects.remove(project)
            if technology_id and not technology_id in project.technologies_ids:
                #technology filter
                projects.remove(project)

        return projects
        

    @staticmethod
    def update(updates: dict, app: Flask) -> List[ProjectModel]:
        return [ProjectServices.update(update, update["id"], app) for update in updates["projects"]]

    @staticmethod
    def delete(ids: List[str], app: Flask) -> List[int]:
        return [ProjectServices.delete(id_, app) for id_ in ids]