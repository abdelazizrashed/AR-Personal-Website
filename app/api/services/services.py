from flask import Flask
from typing import Dict, List

from app.api.services.interfaces import ServiceContentInterface
# from app.api.shared.interfaces import IMGInfoInterface, TechnologyInterface
# from app.api.services.interfaces import ServiceContentInterface
from .models import ServiceModel, ServiceContentModel, ServiceTechnologyModel
from app.api.shared.helpers.services import HelperServices, rm_none_from_dict
from app.api.shared.services import IMGInfoServices


class ServiceContentServices:

    @staticmethod
    def json(content: ServiceContentModel) -> dict:
        if not content: return None
        if content:
            return {
                "title": content.title,
                "paragraph": content.paragraph,
            }
        return None

    @staticmethod
    def from_json(json: dict) -> ServiceContentModel:
        if not json: return
        attr = dict(title=json.get("title"), paragraph=json.get("paragraph"))

        content = ServiceContentModel()
        content.update(attr)
        return content

class ServiceTechnologyServices:

    @staticmethod
    def json(tech: ServiceTechnologyModel) -> dict:
        if not tech: return None
        json_dict = dict()
        json_dict["name"] = tech.name
        json_dict["description"] = tech.description

        return json_dict

    @staticmethod
    def from_json(attrs: dict) -> ServiceTechnologyModel:
        if not attrs: return
        tech = ServiceTechnologyModel()
        tech.name = attrs.get("name")
        tech.description = attrs.get("description")
        return tech

class ServiceContentsServices:

    @staticmethod
    def json(contents: List[ServiceContentModel]) -> List[dict]:
        if not contents: return  []
        return [ServiceContentServices.json(content) for content in contents if  contents ]

    @staticmethod
    def from_json(attrs: List[dict]) -> List[ServiceContentModel]:
        if not attrs: return []
        return [ServiceContentServices.from_json(attr) for attr in attrs if attrs]

class ServiceTechnologiesServices:

    @staticmethod
    def json(techs: List[ServiceTechnologyModel]) -> List[dict]:
        if not techs: return []
        return [ServiceTechnologyServices.json(tech) for tech in  techs if techs]

    @staticmethod
    def from_json(attrs: List[dict]) -> List[ServiceTechnologyModel]:
        if not attrs: return []
        return [ServiceTechnologyServices.from_json(attr) for attr in attrs  if attrs]

class ServiceServices:
    @staticmethod
    def json(service: ServiceModel, storage) -> Dict:
        print("json got  called")
        if not service: return None
        if service:
            return {
                "name": service.name,
                "description": service.description,
                "id": service.id_,
                "importance": service.importance,
                "logo": IMGInfoServices.json(service.logo, storage),
                "projectsIds": service.projects_ids,
                "otherServicesIds": service.other_services_ids,
                "content": ServiceContentsServices.json(service.content),
                "technologies": ServiceTechnologiesServices.json(service.technologies)
            }
        return None

    @staticmethod
    def json_partial(service: ServiceModel,storage) -> dict:
        if not service: return
        print("json  partial got  called")
        if service:
            return {
                "name": service.name,
                "description": service.description,
                "id": service.id_,
                "importance": service.importance,
                "logo": IMGInfoServices.json(service.logo, storage)
            }
        return None
    

    @staticmethod
    def from_json(json: dict, app: Flask) -> ServiceModel:
        if not json: return
        service = ServiceModel()
        service.id_ = json.get('id')
        service.name=json.get("name")
        service.description=json.get("description")
        service.id_=json.get("id")
        service.importance=json.get("importance")
        service.logo=IMGInfoServices.from_json(json.get("logo"), app)
        service.projects_ids=json.get("projectsIds")
        service.other_services_ids=json.get("otherServicesIds")
        service.content=ServiceContentsServices.from_json(json.get("content")) 
        
        service.technologies= ServiceTechnologiesServices.from_json(json.get("technologies"))

        return service

    @staticmethod
    def create(attrs: dict, app: Flask) -> ServiceModel:
        db = HelperServices.get_firebase_database(app)
        id_ = db.child("services").push(attrs)["name"]
        attrs["id"] = id_
        service = ServiceServices.from_json(attrs, app)
        return service

    @staticmethod
    def retreive(id_: str, app: Flask) -> ServiceModel:
        db = HelperServices.get_firebase_database(app)
        result = db.child("services").child(id_).get()
        if not result.val(): return None
        attrs = dict(result.val())
        attrs["id"] = result.key()
        if attrs == None:
            return None
        # print(attrs)
        return ServiceServices.from_json(attrs, app)

    @staticmethod
    def update(updates: dict, id_: str, app: Flask) -> ServiceModel:
        db = HelperServices.get_firebase_database(app)
        updates  = rm_none_from_dict(updates)
        db.child("services").child(id_).update(updates)
        return ServiceServices.retreive(id_,  app)

    @staticmethod
    def delete(id_: str, app: Flask) -> int:
        db = HelperServices.get_firebase_database(app)
        return db.child("services").child(id_).remove()


class ServicesServices:
    @staticmethod
    def json(services: List[ServiceModel], app: Flask) -> List[dict]:
        if not services: return []
        storage = HelperServices.get_firebase_storage(app)
        if services: return [ServiceServices.json(service, storage) for service in services if service]
        return None

    def json_partial(services: List[ServiceModel], app: Flask)-> List[dict]:
        if not services: return []
        storage = HelperServices.get_firebase_storage(app)
        if services: return [ServiceServices.json_partial(service, storage) for service in services if service]
        return None

    @staticmethod
    def from_json(json: List[dict], app) -> list[ServiceModel]:
        if not json: return
        return [ServiceServices.from_json(j,  app) for j in json]

    @staticmethod
    def create(attrs: List[dict], app: Flask) -> List[ServiceModel]:
        return [ServiceServices.create(attr, app) for attr in attrs]

    @staticmethod
    def retreive(app: Flask, ids: List[str] = None,) -> List[ServiceModel]:
        services: List[ServiceModel] = []
        db = HelperServices.get_firebase_database(app)
        results = db.child("services").get()
        if not results.each():return None
        for result in results.each():
            s_attrs = result.val()
            s_attrs["id"] = result.key()
            services.append(ServiceServices.from_json(s_attrs, app))
        for service in services:
            if ids and not service.id_ in ids:
                #id filter
                services.remove(service)
            #*Leave them if you want to implement other filters
            # if service_id and not service_id in project.services_ids:
            #     #service filter
            #     projects.remove(project)
            # if platform_id and not platform_id in project.platforms_ids:
            #     #platform filter
            #     projects.remove(project)
            # if technology_id and not technology_id in project.technologies_ids:
            #     #technology filter
            #     projects.remove(project)
        return services

    @staticmethod
    def update(updates: dict, app: Flask) -> List[ServiceModel]:
        return [ServiceServices.update(rm_none_from_dict(update), update["id"],  app) for update in updates]

    @staticmethod
    def delete(ids: List[str], app: Flask) -> List[int]:
        return [ServiceServices.delete(id_, app) for id_ in ids]

