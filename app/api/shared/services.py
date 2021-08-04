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
    def json(technology: TechnologyModel, app: Flask) -> dict:
        return {
            "name": technology.name,
            "description": technology.description,
        }

    @staticmethod
    def from_json(json: dict) -> TechnologyModel:
        technology = TechnologyModel()
        technology.name = json.get("name")
        technology.description = json.get("name")

        return technology


class PlatformServices:
    @staticmethod
    def json(platform: PlatformModel, app: Flask) -> dict:
        return {
            "name": platform.name,
            "description": platform.description,
        }

    @staticmethod
    def from_json(json: dict) -> PlatformModel:
        platform = PlatformModel()
        platform.name = json.get("name")
        platform.description = json.get("name")

        return platform
