import pyrebase
import json as j
from flask import Flask
from .models import InfoModel, NavbarPagesModel, IMGInfoModel
from .interfaces import InfoInterface
from app.api.shared.helpers.services import HelperServices


class InfoServices:
    @staticmethod
    def json(info: InfoModel, app: Flask) -> dict:
        storage = HelperServices.get_firebase_storage(app)
        # print(str(info.home_laptop_img_info))
        # print(info.home_laptop_img_info.cloud_path)
        # print(info.home_laptop_img_info.alt)
        # print(info.home_tablet_img_info.cloud_path)
        # print(info.home_tablet_img_info.alt)
        # print(info.home_phone_img_info.cloud_path)
        # print(info.home_phone_img_info.alt)
        if info:
            return {
                "navbarPages": NavbarPageServices.json(info.navbar_pages),
                "homePageIntro": info.home_page_intro,
                "homeLaptopImgInfo": IMGInfoServices.json(
                    info.home_laptop_img_info, app
                ),
                "homeTabletImgInfo": IMGInfoServices.json(
                    info.home_tablet_img_info, app
                ),
                "homePhoneImgInfo": IMGInfoServices.json(info.home_phone_img_info, app),
                "A_RashedAboutPicInfo": IMGInfoServices.json(
                    info.ar_about_pic_info, app
                ),
                "A_RashedAboutLongParag": info.ar_about_long_parag,
                "A_RashedAboutShortParag": info.ar_about_short_parag,
                "A_RashedEmail": info.ar_email,
                "A_RashedPhoneNo": info.ar_phone_no,
            }
        return None

    @staticmethod
    def from_json(json: dict) -> InfoModel:
        # print(json)
        info_attr = dict(
            navbar_pages=json.get("navbarPages"),
            home_page_intro=json.get("homePageIntro"),
            home_laptop_img_info=IMGInfoServices.from_json(
                json.get("homeLaptopImgInfo")
            ),
            home_tablet_img_info=IMGInfoServices.from_json(
                json.get("homeTabletImgInfo")
            ),
            home_phone_img_info=IMGInfoServices.from_json(json.get("homePhoneImgInfo")),
            ar_about_pic_info=IMGInfoServices.from_json(
                json.get("A_RashedAboutPicInfo")
            ),
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
        # print(attrs)
        attrs = db.child("Info").set(dict(attrs))
        # print(attrs)
        info = InfoServices.from_json(attrs)
        return info


class NavbarPageServices:
    @staticmethod
    def json(navbar_pages: NavbarPagesModel) -> dict:
        if navbar_pages:
            return {
                "home": True,
                "projects": True,
                "services": True,
                "contact": navbar_pages.contact,
                "resume": navbar_pages.resume,
                "certificates": navbar_pages.certificates,
                "about": navbar_pages.about,
            }
        return None

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


class IMGInfoServices:
    @staticmethod
    def json(img_info: IMGInfoModel, app: Flask) -> dict:
        storage = HelperServices.get_firebase_storage(app)
        # print(img_info)

        return {
            "url": HelperServices.get_url_from_cloud_path(img_info.cloud_path, storage),
            "alt": img_info.alt,
        }
        # if img_info:
        # return None

    @staticmethod
    def from_json(json: dict) -> IMGInfoModel:
        img_info = IMGInfoModel()
        img_info.cloud_path = json.get("cloudPath")
        img_info.alt = json.get("alt")
        return img_info