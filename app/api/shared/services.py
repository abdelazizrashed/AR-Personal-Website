
from typing import List
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
    def json_all(technology: TechnologyModel) -> dict:
        return {
            "name": technology.name,
            "description": technology.description,
            "id": technology.id_,
        }

    @staticmethod
    def json_partial(technology: TechnologyModel) -> dict:
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
    @staticmethod
    def create(attrs: dict, app: Flask) -> TechnologyModel:
        raise NotImplementedError

    @staticmethod
    def update(updates: dict, id_: str, app: Flask) -> TechnologyModel:
        raise NotImplementedError

    @staticmethod
    def retrieve(id_: str, app: Flask) -> TechnologyModel:
        raise NotImplementedError

    @staticmethod
    def delete(id_: str, app: Flask):
        raise NotImplementedError

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
    @staticmethod
    def create(attrs: dict, app: Flask) -> PlatformModel:
        raise NotImplementedError

    @staticmethod
    def update(updates: dict, app: Flask) -> PlatformModel:
        raise NotImplementedError

    @staticmethod
    def retrieve(id_: str, app: Flask) -> PlatformModel:
        raise NotImplementedError

    @staticmethod
    def delete(id_: str, app: Flask):
        raise NotImplementedError


class TechnologiesServices:

    @staticmethod
    def json_all(technologies: List[TechnologyModel]) -> dict:
        techs_key = "technologies"
        technologies_dict = {techs_key: []}
        for tech in technologies:
            technologies_dict[techs_key].append(TechnologyServices.json_all(tech))
        return technologies_dict

    @staticmethod
    def json_partial(technologies: List[TechnologyModel]) -> dict:
        techs_key = "technologies"
        technologies_dict = {techs_key: []}
        for tech in technologies:
            technologies_dict[techs_key].append(TechnologyServices.json_partial(tech))
        return technologies_dict

    @staticmethod
    def from_json(json: dict) -> List[TechnologyModel]:
        techs = []
        for json_dict in json["technologies"]:
            techs.append(TechnologyServices.from_json(json_dict))

        return techs

    # Todo: impelement the CRUD methods
    @staticmethod
    def create(attrs: dict, app: Flask) -> List[TechnologyModel]:
        raise NotImplementedError

    @staticmethod
    def update(updates: dict, app: Flask) -> List[TechnologyModel]:
        raise NotImplementedError

    @staticmethod
    def retrieve(app: Flask, ids: List[str] = None) -> List[TechnologyModel]:
        raise NotImplementedError

    @staticmethod
    def delete(ids: List[str], app: Flask):
        raise NotImplementedError


class PlatformsServices:

    @staticmethod
    def json_all(platforms: List[PlatformModel]) -> dict:
        plat_key = "platforms"
        plat_dict = {plat_key: []}
        for platform in platforms:
            plat_dict[plat_key].append(PlatformServices.json_all(platform))
        return plat_dict

    @staticmethod
    def json_partial(platforms: List[PlatformModel]) -> dict:
        plat_key = "platforms"
        plat_dict = {plat_key: []}
        for platform in platforms:
            plat_dict[plat_key].append(PlatformServices.json_partial(platform))
        return plat_dict

    @staticmethod
    def from_json(json: dict) -> List[PlatformModel]:
        plats = []
        for plat_json in json["platforms"]:
            plats.append(PlatformServices.from_json(plat_json))

        return plats

    # Todo: impelement the CRUD methods
    @staticmethod
    def create(attrs: dict, app: Flask) -> List[PlatformModel]:
        raise NotImplementedError

    @staticmethod
    def update(updates: dict, ids:List[str], app: Flask) -> List[PlatformModel]:
        raise NotImplementedError

    @staticmethod
    def retrieve(app: Flask, ids: List[str] = None) -> List[PlatformModel]:
        raise NotImplementedError

    @staticmethod
    def delete(ids: List[str], app: Flask):
        raise NotImplementedError