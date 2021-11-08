from typing import List
from flask import Flask
from app.api.shared.helpers.services import HelperServices
from app.api.shared.models import IMGInfoModel, TechnologyModel, PlatformModel
from app.api.shared.helpers.services import HelperServices
from werkzeug.datastructures import FileStorage


class IMGInfoServices:
    @staticmethod
    def json(img_info: IMGInfoModel, app: Flask) -> dict:
        storage = HelperServices.get_firebase_storage(app)

        return {
            "src": HelperServices.get_url_from_cloud_path(img_info.cloud_path, storage),
            "alt": img_info.alt,
            "caption": img_info.caption
        }

    @staticmethod
    def from_json(json: dict, file: FileStorage = None, app: Flask = None) -> IMGInfoModel:
        """
        The upload functionality of this method is deprecated and it will be removed.
        """
        img_info = IMGInfoModel()
        #Todo: delete the upload functionality
        # if file and app:
        #     img_info.cloud_path = HelperServices.upload_file(file, app)
        # if file and not app:
        #     raise AttributeError("If you intend to upload an image you should include the flask app")
        # else:
        #     if json.get("img"):
        #         img_info.cloud_path = HelperServices.upload_file(file, app)
        #     elif json.get("couldPath"):
        img_info.cloud_path = json.get("cloudPath")

        img_info.alt = json.get("alt")
        img_info.caption = json.get("caption")
        return img_info

    @staticmethod
    def upload(img: FileStorage,app:Flask) -> str:
        cloud_path = HelperServices.upload_file(img, app)
        return cloud_path


class TechnologyServices:
    @staticmethod
    def json(technology: TechnologyModel) -> dict:
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

    @staticmethod
    def create(attrs: dict, app: Flask) -> TechnologyModel:
        db = HelperServices.get_firebase_database(app)
        id_ = db.child("technologies").push(attrs)["name"]
        attrs["id"] = id_
        platform = TechnologyServices.from_json(attrs)
        return platform

    @staticmethod
    def update(updates: dict, id_: str, app: Flask) -> TechnologyModel:
        db = HelperServices.get_firebase_database(app)
        attrs = db.child("technologies").child(id_).update(updates)
        if attrs == None:
            return None
        return TechnologyServices.from_json(attrs)


    @staticmethod
    def retrieve(id_: str, app: Flask) -> TechnologyModel:
        db = HelperServices.get_firebase_database(app)
        result = db.child("technologies").child(id_).get()
        attrs = dict(result.val())
        attrs["id"] = result.key()
        if attrs == None:
            return None
        return TechnologyServices.from_json(attrs)


    @staticmethod
    def delete(id_: str, app: Flask) -> int:
        db = HelperServices.get_firebase_database(app)
        return db.child("technologies").child(id_).remove()

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

    @staticmethod
    def create(attrs: dict, app: Flask) -> PlatformModel:
        db = HelperServices.get_firebase_database(app)
        id_ = db.child("platforms").push(attrs)["name"]
        attrs["id"] = id_
        platform = PlatformServices.from_json(attrs)
        return platform

    @staticmethod
    def update(updates: dict, id_: str, app: Flask) -> PlatformModel:
        db = HelperServices.get_firebase_database(app)
        attrs = db.child("platforms").child(id_).update(updates)
        if attrs == None:
            return None
        return PlatformServices.from_json(attrs)


    @staticmethod
    def retrieve(id_: str, app: Flask) -> PlatformModel:
        db = HelperServices.get_firebase_database(app)
        result = db.child("platforms").child(id_).get()
        attrs = dict(result.val())
        attrs["id"] = result.key()
        if attrs == None:
            return None
        return PlatformServices.from_json(attrs)


    @staticmethod
    def delete(id_: str, app: Flask) -> int:
        db = HelperServices.get_firebase_database(app)
        return db.child("platforms").child(id_).remove()

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

    @staticmethod
    def create(attrs: dict, app: Flask) -> List[TechnologyModel]:
        techs = []
        for tech in attrs["technologies"]:
            techs.append(TechnologyServices.create(tech, app))
        return techs

    @staticmethod
    def update(updates: dict, app: Flask) -> List[TechnologyModel]:
        techs = []
        for tech in updates["technologies"]:
            id_ = tech.pop("id")
            techs.append(TechnologyServices.update(tech, id_, app))

        return techs


    @staticmethod
    def retrieve(app: Flask, ids: List[str] = None) -> List[TechnologyModel]:
        techs = []
        for id_ in ids:
            techs.append(TechnologyServices.retrieve(id_, app))
        return techs

    @staticmethod
    def delete(ids: List[str], app: Flask) -> dict:
        res = {"result": []}
        is_success = False
        for id_ in ids:
            status_code = TechnologyServices.delete(id_, app)
            if status_code == 200:
                res["result"].append({"message": "Succeeded", "id": id_})
                is_success = True
            else:
                res["result"].append({"message": "Failed", "id": id_})
        sc = 200 if is_success else status_code
        return res, sc


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
    def delete(ids: List[str], app: Flask) -> dict:
        raise NotImplementedError

    @staticmethod
    def create(attrs: dict, app: Flask) -> List[PlatformModel]:
        platforms = []
        for platform in attrs["platforms"]:
            platforms.append(PlatformServices.create(platform, app))
        return platforms

    @staticmethod
    def update(updates: dict, app: Flask) -> List[PlatformModel]:
        platforms = []
        for platform in updates["platforms"]:
            id_ = platform.pop("id")
            platforms.append(PlatformServices.update(platform, id_, app))
        return platforms


    @staticmethod
    def retrieve(app: Flask, ids: List[str] = None) -> List[PlatformModel]:
        return [PlatformServices.retrieve(id_, app) for id_ in ids]

    @staticmethod
    def delete(ids: List[str], app: Flask) -> dict:
        return [PlatformServices.delete(id_, app) for id_ in ids]