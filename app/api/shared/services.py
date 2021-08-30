from flask import Flask
from app.api.shared.helpers.services import HelperServices
from app.api.shared.models import IMGInfoModel, TechnologyModel, PlatformModel


class IMGInfoServices:
    @staticmethod
    def json(img_info: IMGInfoModel, app: Flask) -> dict:
        storage = HelperServices.get_firebase_storage(app)

        return {
            "src": HelperServices.get_url_from_cloud_path(img_info.cloud_path, storage),
            "alt": img_info.alt,
        }

    @staticmethod
    def from_json(json: dict) -> IMGInfoModel:
        img_info = IMGInfoModel()
        img_info.cloud_path = json.get("cloudPath")
        img_info.alt = json.get("alt")
        return img_info


class TechnologyServices:
    @staticmethod
    def json_all(technology: TechnologyModel, app: Flask) -> dict:
        return {
            "name": technology.name,
            "description": technology.description,
            "id": technology.id_,
        }

    @staticmethod
    def json_partial(technology: TechnologyModel, app: Flask) -> dict:
        return {
            "name": technology.name,
            "id": technology.id_,
        }

    @staticmethod
    def from_json(json: dict) -> TechnologyModel:
        technology = TechnologyModel()
        technology.name = json.get("name")
        technology.description = json.get("description")
        technology.id_ = json.get("id")

        return technology

    # Todo: impelement the CRUD methods


class PlatformServices:
    @staticmethod
    def json_all(platform: PlatformModel, app: Flask) -> dict:
        return {
            "name": platform.name,
            "description": platform.description,
            "id": platform.id_,
        }

    @staticmethod
    def json_partial(platform: PlatformModel, app: Flask) -> dict:
        return {
            "name": platform.name,
            "id": platform.id_,
        }

    @staticmethod
    def from_json(json: dict) -> PlatformModel:
        platform = PlatformModel()
        platform.name = json.get("name")
        platform.description = json.get("description")
        platform.id_ = json.get("id")

        return platform

    # Todo: impelement the CRUD methods
