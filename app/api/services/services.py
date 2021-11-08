from flask import Flask
from typing import Dict, List

from app.api.services.interfaces import ServiceContentInterface
# from app.api.shared.interfaces import IMGInfoInterface, TechnologyInterface
# from app.api.services.interfaces import ServiceContentInterface
from .models import ServiceModel, ServiceContentModel, ServiceTechnologyModel
from app.api.shared.helpers.services import HelperServices
from app.api.shared.services import IMGInfoServices


class ServiceContentServices:

    @staticmethod
    def json(content: ServiceContentModel) -> dict:
        if content:
            return {
                "title": content.title,
                "paragraph": content.paragraph,
            }
        return None

    @staticmethod
    def from_json(json: dict) -> ServiceContentModel:
        attr = dict(title=json.get("title"), paragraph=json.get("paragraph"))

        content = ServiceContentModel()
        content.update(attr)
        return content

class ServiceTechnologyServices:

    @staticmethod
    def json(tech: ServiceTechnologyModel) -> dict:
        json_dict = dict()
        json_dict["name"] = tech.name
        json_dict["description"] = tech.description

        return json_dict

    @staticmethod
    def from_json(attrs: dict) -> ServiceTechnologyModel:
        tech = ServiceTechnologyModel()
        tech.name = attrs.get("name")
        tech.description = attrs.get("description")
        return tech

class ServiceContentsServices:

    @staticmethod
    def json(contents: List[ServiceContentModel]) -> List[dict]:
        return [ServiceContentServices.json(content) for content in contents]

    @staticmethod
    def from_json(attrs: List[dict]) -> List[ServiceContentModel]:
        return [ServiceContentServices.from_json(attr) for attr in attrs]

class ServiceTechnologiesServices:

    @staticmethod
    def json(techs: List[ServiceTechnologyModel]) -> List[dict]:
        return [ServiceTechnologyServices.json(tech) for tech in  techs]

    @staticmethod
    def from_json(attrs: List[dict]) -> List[ServiceTechnologyModel]:
        return [ServiceTechnologyServices.from_json(attr) for attr in attrs]

class ServiceServices:
    @staticmethod
    def json(service: ServiceModel, app: Flask) -> Dict:
        if service:
            return {
                "name": service.name,
                "description": service.description,
                "id": service.id_,
                "importance": service.importance,
                "logo": IMGInfoServices.json(service.logo, app),
                "projects": service.projects,
                "otherServices": service.other_services,
                "content": [ServiceContentServices.json(x) for x in service.content],
                "technologies": ServiceTechnologiesServices.json(service.technologies)
            }
        return None

    @staticmethod
    def from_json(json: dict) -> ServiceModel:
        service = ServiceModel()
        service.name=json.get("name"),
        service.description=json.get("description"),
        service.id_=json.get("id"),
        service.importance=json.get("importance"),
        service.logo=IMGInfoServices.from_json(json.get("logo")),
        service.projects=json.getlist("projects"),
        service.other_services=json.getlist("otherServices"),
        service.content=[
            ServiceContentServices.from_json(x) for x in json.getlist("content")
        ],
        service.technologies= ServiceTechnologiesServices.from_json(json.getlist("technologies"))

        return service

    @staticmethod
    def create(attrs: dict, app: Flask) -> ServiceModel:
        db = HelperServices.get_firebase_database(app)
        id_ = db.child("services").push(attrs)["name"]
        attrs["id"] = id_
        service = ServiceServices.from_json(attrs)
        return service

    @staticmethod
    def retreive(id_: str, app: Flask) -> ServiceModel:
        db = HelperServices.get_firebase_database(app)
        attrs = db.child("services").child(id_).get()
        if attrs == None:
            return None
        return ServiceServices.from_json(attrs)

    @staticmethod
    def update(updates: dict, id_: str, app: Flask) -> ServiceModel:
        db = HelperServices.get_firebase_database(app)
        attrs = db.child("services").child(id_).update(updates)
        if attrs == None:
            return None
        attrs["id"] = id_
        return ServiceServices.from_json(attrs)

    @staticmethod
    def delete(id_: str, app: Flask) -> ServiceModel:
        db = HelperServices.get_firebase_database(app)
        res = db.child("services").child(id_).remove()
        return res.status_code


class ServicesServices:

    