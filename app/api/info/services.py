import pyrebase
from flask import Flask
from .models import InfoModel, NavbarPagesModel
from .interfaces import InfoInterface
from app.api.shared.helpers.services import HelperServices


class InfoServices:
    @staticmethod
    def json(info: InfoModel, app: Flask) -> dict:
        storage = HelperServices.get_firebase_storage(app)
        print(info.navbar_pages)
        return {
            "navbarPages": NavbarPageServices.json(info.navbar_pages),
            "homePageIntro": info.home_page_intro,
            "homeLaptopImgUrl": HelperServices.get_url_from_cloud_path(
                info.home_laptop_img_cloud_path, storage
            ),
            "homeTabletImgUrl": HelperServices.get_url_from_cloud_path(
                info.home_tablet_img_cloud_path, storage
            ),
            "homePhoneImgUrl": HelperServices.get_url_from_cloud_path(
                info.home_phone_img_cloud_path, storage
            ),
            "A_RashedAboutPicUrl": HelperServices.get_url_from_cloud_path(
                info.ar_about_pic_cloud_path, storage
            ),
            "A_RashedAboutLongParag": info.ar_about_long_parag,
            "A_RashedAboutShortParag": info.ar_about_short_parag,
            "A_RashedEmail": info.ar_email,
            "A_RashedPhoneNo": info.ar_phone_no,
        }

    @staticmethod
    def from_json(json: dict) -> InfoModel:
        info_attr = dict(
            navbar_pages=json.get("navbarPages"),
            home_page_intro=json.get("homePageIntro"),
            home_laptop_img_cloud_path=json.get("homeLaptopImgCloudPath"),
            home_tablet_img_cloud_path=json.get("homeTabletImgCloudPath"),
            home_phone_img_cloud_path=json.get("homePhoneImgCloudPath"),
            ar_about_pic_cloud_path=json.get("A_RashedAboutPicCloudPath"),
            ar_about_long_parag=json.get("A_RashedAboutLongParag"),
            ar_about_short_parag=json.get("A_RashedAboutShortParag"),
            ar_email=json.get("A_RashedEmail"),
            ar_phone_no=json.get("A_RashedPhoneNo"),
        )
        new_info = InfoModel()
        new_info.update(info_attr)
        return new_info

    @staticmethod
    def retrieve(app: Flask) -> InfoModel:
        db = HelperServices.get_firebase_database(app)
        results = db.child("Info").get()
        attrs = dict(results.val())
        info = InfoServices.from_json(attrs)
        return info

    @staticmethod
    def update(updates: dict, app: Flask) -> InfoModel:
        db = HelperServices.get_firebase_database(app)
        attrs = db.child("Info").update(dict(updates))
        info = InfoServices.from_json(attrs)
        return info

    @staticmethod
    def create(attrs: dict, app: Flask) -> InfoModel:
        db = HelperServices.get_firebase_database(app)
        attrs = db.child("Info").set(dict(attrs))
        info = InfoServices.from_json(attrs)
        return info


class NavbarPageServices:
    @staticmethod
    def json(navbar_pages: NavbarPagesModel) -> dict:
        return {
            "home": True,
            "projects": True,
            "services": True,
            "contact": navbar_pages.contact,
            "resume": navbar_pages.resume,
            "certificates": navbar_pages.certificates,
            "about": navbar_pages.about,
        }

    @staticmethod
    def from_json(json: dict) -> NavbarPagesModel:
        attrs = {
            "home": True,
            "projects": True,
            "services": True,
            "contact": json.contact,
            "resume": json.resume,
            "certificates": json.certificates,
            "about": json.about,
        }

        pages = NavbarPagesModel()
        pages.update(attrs)
        return pages