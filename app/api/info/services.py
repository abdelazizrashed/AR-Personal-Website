from flask import Flask
from .models import InfoModel, NavbarPagesModel, IMGInfoModel
from .interfaces import InfoInterface
from app.api.shared.helpers.services import HelperServices
from app.api.shared.services import IMGInfoServices


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
            return_info = dict()
            if info.navbar_pages :
                return_info["navbarPages"] = NavbarPageServices.json(info.navbar_pages),
                
            if info.home_page_intro:
                return_info["homePageIntro"] =  info.home_page_intro,
                
            if info.home_laptop_img_info :
                return_info["homeLaptopImgInfo"] = IMGInfoServices.json(
                    info.home_laptop_img_info, app
                ),
                
            if info.home_tablet_img_info :
                return_info["homeTabletImgInfo"] = IMGInfoServices.json(
                    info.home_tablet_img_info, app
                ),
                
            if info.home_phone_img_info :
                return_info["homePhoneImgInfo"] = IMGInfoServices.json(info.home_phone_img_info, app),
                
            if info.ar_about_pic_info :
                return_info["A_RashedAboutPicInfo"] = IMGInfoServices.json(
                    info.ar_about_pic_info, app
                ),
                
            if info.ar_about_long_parag :
                return_info["A_RashedAboutLongParag"] = info.ar_about_long_parag,
                
            if info.ar_about_short_parag :
                return_info["A_RashedAboutShortParag"] = info.ar_about_short_parag,
                
            if info.ar_email :
                return_info["A_RashedEmail"] = info.ar_email,
                
            if info.ar_phone_no :
                return_info["A_RashedPhoneNo"] = info.ar_phone_no,
                
            return return_info
        return None

    @staticmethod
    def from_json(json: dict) -> InfoModel:
        """
        This method is used to change the data which is in a dictionary format to an InfoModel object and return it.
        """
        # print(json)
        info_attr = dict()
        if json.get("navbarPages"):
            info_attr["navbar_pages"]=json.get("navbarPages")

        if json.get("homePageIntro"):
            info_attr["home_page_intro"]=json.get("homePageIntro")

        if json.get("homeLaptopImgInfo"):
            info_attr["home_laptop_img_info"]=IMGInfoServices.from_json(
                json.get("homeLaptopImgInfo")
            )

        if json.get("homeTabletImgInfo"):
            info_attr["home_tablet_img_info"]=IMGInfoServices.from_json(
                json.get("homeTabletImgInfo")
            )

        if json.get("homePhoneImgInfo"):
            info_attr["home_phone_img_info"]=IMGInfoServices.from_json(json.get("homePhoneImgInfo"))

        if json.get("A_RashedAboutPicInfo"):
            info_attr["ar_about_pic_info"]=IMGInfoServices.from_json(
                json.get("A_RashedAboutPicInfo")
            )

        if json.get("A_RashedAboutLongParag"):
            info_attr["ar_about_long_parag"]=json.get("A_RashedAboutLongParag")

        if json.get("A_RashedAboutShortParag"):
            info_attr["ar_about_short_parag"]=json.get("A_RashedAboutShortParag")

        if json.get("A_RashedEmail"):
            info_attr["ar_email"]=json.get("A_RashedEmail")

        if json.get("A_RashedPhoneNo"):
            info_attr["ar_phone_no"]=json.get("A_RashedPhoneNo")
            ar_phone_no=json.get("A_RashedPhoneNo"),

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
        if attrs == None:
            return None
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