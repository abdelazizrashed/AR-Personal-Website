from flask import Flask
from typing import Dict, List
from app.api.shared.interfaces import IMGInfoInterface, TechnologyInterface
from app.api.services.interfaces import ServiceContentInterface
from .models import ServiceModel, ServiceContentModel
from app.api.shared.helpers.services import HelperServices
from app.api.shared.services import IMGInfoServices, TechnologyServices


class ServiceServices:
    @staticmethod
    def json(service: ServiceModel, app: Flask) -> Dict:
        storage = HelperServices.get_firebase_storage(app)
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
                "technologies": [
                    TechnologyServices.json_all(x) for x in service.technologies
                ],
            }
        return None

    @staticmethod
    def from_json(json: Dict) -> ServiceModel:
        attrs = dict(
            name=json.get("name"),
            description=json.get("description"),
            id_=json.get("id"),
            importance=json.get("importance"),
            logo=IMGInfoServices.from_json(json.get("logo")),
            projects=json.getlist("projects"),
            other_services=json.getlist("otherServices"),
            content=[
                ServiceContentServices.from_json(x) for x in json.getlist("content")
            ],
            technologies=[
                TechnologyServices.from_json(x) for x in json.getlist("technologies")
            ],
        )

        service = ServiceModel()
        service.update(attrs)
        return service

    @staticmethod
    def create(attrs: dict, app: Flask) -> ServiceModel:
        raise NotImplementedError

    @staticmethod
    def retreive(id_: str, app: Flask) -> ServiceModel:
        raise NotImplementedError

    @staticmethod
    def update(attrs: dict, app: Flask) -> ServiceModel:
        raise NotImplementedError

    @staticmethod
    def delete(attrs: dict, app: Flask) -> ServiceModel:
        raise NotImplementedError


class ServiceContentServices:
    title: str
    paragraph: str

    @staticmethod
    def json(content: ServiceContentModel) -> Dict:
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