from typing import List

from flask.app import Flask
from werkzeug.exceptions import NotFound
from app.api.services.services import ServiceServices

from app.api.shared.models import PlatformModel, TechnologyModel
from .models import YouTubeVidModel, DetailModel, ProjectModel
from app.api.shared.services import IMGInfoServices, PlatformServices, PlatformsServices, TechnologiesServices, TechnologyServices
from app.api.shared.helpers.services import HelperServices, rm_none_from_dict


#Todo: Images upload is faulted as well as technologies and platforms have a second look on how you would change it. I commented them so you won't forget

class YouTubeVidServices:

    @staticmethod 
    def json(vid: YouTubeVidModel) -> dict:
        if not vid: return None
        return {
            "src": vid.src,
            "title": vid.title
        }

    @staticmethod
    def from_json(json: dict) -> YouTubeVidModel:
        if not json: return 
        vid = YouTubeVidModel()
        vid.src = json.get("src")
        vid.title = json.get("title")

        return vid


class DetailServices:

    @staticmethod
    def json(detail: DetailModel) -> dict:
        if not detail: return None
        return {
            "name": detail.name,
            "description": detail.description
        }

    @staticmethod
    def from_json(json: dict) ->DetailModel:
        if not json: return
        
        detail = DetailModel()

        detail.name = json.get("name")
        detail.description = json.get("description")

        return detail

class YouTubeVidsServices:

    @staticmethod 
    def json(vids: List[YouTubeVidModel]) -> dict:
        vids_lbl = "vids"

        return_dict = {vids_lbl: []}
        if not vids:  return return_dict
        for vid in vids:
            return_dict[vids_lbl].append(YouTubeVidServices.json(vid))
        
        return return_dict

    @staticmethod
    def from_json(json: dict) -> List[YouTubeVidModel]:
        if not json: return
        vids = []

        for vid_json in json.get("vids"):
            vids.append(YouTubeVidServices.from_json(vid_json))

        return vids


class DetailsServices:

    @staticmethod
    def json(details: List[DetailModel]) -> dict:
        
        details_lbl = "details"

        json = {details_lbl: []}

        if not details: return json

        for detail in details:
            json[details_lbl].append(DetailServices.json(detail))

        return json

    @staticmethod
    def from_json(json: dict) ->List[DetailModel]:
        if not json: return
        
        details = []

        for d_json in json["details"]:
            details.append(DetailServices.from_json(d_json))

        return details


class ProjectServices:

    @staticmethod 
    def json(project: ProjectModel, app: Flask, storage, platforms: List[PlatformModel] = None, technologies: List[TechnologyModel] = None) -> dict:
        if not project: return None
        json = dict()  
        json["name"] = project.name
        json["id"] = project.id_
        if project.platforms_ids: 
            if platforms:
                json["platforms"] = [platform.name for platform in platforms if platform.id_ in project.platforms_ids]
            else:
                json["platforms"] = [PlatformServices.retrieve(id_, app).name for id_ in project.platforms_ids]
        if project.technologies_ids:
            if  technologies:
                json["technologies"] = [technology.name for  technology in  technologies if technology.id_ in project.technologies_ids]
            else:
                json["technologies"] = [TechnologyServices.retrieve(id_, app).name for id_ in project.technologies_ids]
        json["img"] = IMGInfoServices.json(project.img, storage)
        json["description"] = project.description
        json["githubUrl"] = project.github_url
        json["appStoreUrl"] = project.app_store_url
        json["googlePlayStoreUrl"] = project.google_play_store_url
        json["websiteUrl"] = project.website_url
        json["youtubeVid"] = YouTubeVidServices.json(project.youtube_vid)
        json["services"] = [ServiceServices.json_partial(ServiceServices.retreive(id_, app), storage) for id_ in project.services_ids]
        json["imgs"] = [IMGInfoServices.json(img, storage) for img in project.imgs]
        if project.related_projects_ids:
            json["relatedProjects"] = ProjectsServices.json_partial(ProjectsServices.retrieve(app, ids = project.related_projects_ids), app)
        json["detailedServices"] = DetailsServices.json(project.detailed_services)
        json["detailedTechnologies"] = DetailsServices.json(project.detailed_technologies)
        json["detailedPlatforms"] = DetailsServices.json(project.detailed_platforms)
        return json

    @staticmethod
    def json_partial(project: ProjectModel, app: Flask, storage, platforms: List[PlatformModel] = None, technologies: List[TechnologyModel] = None) -> dict:
        if not project: return None
        json = dict()
        json["name"] = project.name
        if project.platforms_ids: 
            if platforms:
                json["platforms"] = [platform.name for platform in platforms if platform.id_ in project.platforms_ids]
            else:
                json["platforms"] = [PlatformServices.retrieve(id_, app).name for id_ in project.platforms_ids]
        if project.technologies_ids:
            if  technologies:
                json["technologies"] = [technology.name for  technology in  technologies if technology.id_ in project.technologies_ids]
            else:
                json["technologies"] = [TechnologyServices.retrieve(id_, app).name for id_ in project.technologies_ids]
        
        json["img"] = IMGInfoServices.json(project.img, storage)
        json["id"] = project.id_
        return json

    @staticmethod
    def from_json(json: dict, app: Flask) -> ProjectModel:
        if not json: return
        project = ProjectModel()
        json  = rm_none_from_dict(json)
        project.name =json.get("name")
        project.id_ =json.get("id")
        project.platforms_ids =json.get("platformsIds")
        project.technologies_ids =json.get("technologiesIds") 
        project.img =IMGInfoServices.from_json(json.get("img"),  app)
        project.description =json.get("description") 
        project.github_url =json.get("githubUrl") 
        project.app_store_url =json.get("appStoreUrl")
        project.google_play_store_url =json.get("googlePlayStoreUrl") 
        project.website_url =json.get("websiteUrl") 
        project.youtube_vid =YouTubeVidServices.from_json(json.get("youtubeVid"))
        project.services_ids =json.get("servicesIds") 
        
        if  json.get("imgs"): project.imgs =[IMGInfoServices.from_json(img_json, app) for img_json in json.get("imgs")]
        else: project.imgs = []
        project.related_projects_ids =json.get("relatedProjectsIds")
        if json.get("detailedServices"):
            project.detailed_services =[DetailServices.from_json(j) for j in json.get("detailedServices") ]
        else: project.detailed_services = []
        if json.get("detailedTechnologies"):project.detailed_technologies =[DetailServices.from_json(j) for j in json.get("detailedTechnologies") ]
        else:  project.detailed_technologies = []
        if json.get("detailedPlatforms"):project.detailed_platforms =[DetailServices.from_json(j) for j in json.get("detailedPlatforms") ]
        else:  project.detailed_platforms = []
        return project



    #*CRUD methods
    @staticmethod
    def create(attr: dict, app: Flask) -> ProjectModel:
        db = HelperServices.get_firebase_database(app)
        id_ = db.child("projects").push(attr)["name"]
        attr["id"] = id_
        project = ProjectServices.from_json(attr, app)
        return project

    @staticmethod
    def retrieve(id_: dict, app: Flask) -> ProjectModel:
        db = HelperServices.get_firebase_database(app)
        result = db.child("projects").child(id_).get()
        if not result.val(): return  None
        # print(result.val().get("detailedServices"))
        attrs = dict(result.val())
        attrs["id"] = result.key()
        if attrs == None:
            return None
        return ProjectServices.from_json(attrs, app)

    @staticmethod
    def update(updates: dict, id_: str, app: Flask) -> ProjectModel:
        db = HelperServices.get_firebase_database(app)
        updates  = rm_none_from_dict(updates)
        db.child("projects").child(id_).update(updates)
        return ProjectServices.retrieve(id_, app)

    @staticmethod
    def delete(id_: str, app: Flask) -> int:
        db = HelperServices.get_firebase_database(app)
        return db.child("projects").child(id_).remove()


class ProjectsServices:

    @staticmethod 
    def json(projects: List[ProjectModel], app: Flask) -> dict:
        if not projects: return {"projects": []}
        from time  import time
        t0= time()
        platforms = PlatformsServices.retrieve(app)
        t1= time()
        print(f"platfroms  {t1-t0} seconds")
        technologies = TechnologiesServices.retrieve(app)
        t2 =  time()
        print(f"technologies {t2-t1} seconds")
        storage = HelperServices.get_firebase_storage(app)
        t4= time()
        print(f"storage  {t4-t2} seconds")
        print(f"total {t4-t0} seconds")
        return {"projects": [ProjectServices.json(project, app, storage, platforms, technologies) for project in projects]}


    @staticmethod
    def json_partial(projects: List[ProjectModel], app: Flask) -> dict:
        if not projects: return {"projects": []}
        platforms = PlatformsServices.retrieve(app)
        technologies = TechnologiesServices.retrieve(app)
        storage = HelperServices.get_firebase_storage(app)
        return {"projects": [ProjectServices.json_partial(project, app, storage, platforms, technologies) for project in projects]}

    @staticmethod
    def from_json(json: dict, app) -> List[ProjectModel]:
        if not json: return
        return [ProjectServices.from_json(p_json, app) for p_json in json["projects"]]

    #CRUD methods
    @staticmethod
    def create(attr: dict, app: Flask) -> List[ProjectModel]:
        return [ProjectServices.create(p_attrs, app) for p_attrs in attr["projects"]]

    @staticmethod
    def retrieve(app: Flask, ids: List[str] = None, service_id: str = None, platform_id: str = None, technology_id: str = None) -> List[ProjectModel]:
        projects: List[ProjectModel] = []
        db = HelperServices.get_firebase_database(app)
        results = db.child("projects").get()
        if not results.each(): return None
        for result in results.each():
            p_attrs = dict(result.val())
            p_attrs["id"] = result.key()
            projects.append(ProjectServices.from_json(p_attrs, app))
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
        return [ProjectServices.update(rm_none_from_dict(update), update["id"], app) for update in updates["projects"]]

    @staticmethod
    def delete(ids: List[str], app: Flask) -> List[int]:
        return [ProjectServices.delete(id_, app) for id_ in ids]