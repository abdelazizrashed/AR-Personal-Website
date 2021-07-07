from .models import InfoModel, NavbarPagesModel


class InfoServices:
    @staticmethod
    def json(info: InfoModel):
        return {
            "navbarPages": NavbarPageServices.json(info.navbar_pages),
            "homePageIntro": info.home_page_intro,
            "homeLaptopImgUrl": info.home_laptop_img_url,
            "homeTabletImgUrl": info.home_tablet_img_url,
            "homePhoneImgUrl": info.home_phone_img_url,
            "abdelazizRashedAboutPicUrl": info.abdelaziz_rashed_about_pic_url,
            "abdelazizRashedAboutLongParag": info.abdelaziz_rashed_about_long_parag,
            "abdelazizRashedAboutShortParag": info.abdelaziz_rashed_about_short_parag,
            "abdelazizRashedEmail": info.abdelaziz_rashed_email,
            "abdelazizRashedPhoneNo": info.abdelaziz_rashed_phone_no,
        }


class NavbarPageServices:
    @staticmethod
    def json(navbar_pages: NavbarPagesModel):
        return {
            "home": True,
            "projects": True,
            "services": True,
            "contact": navbar_pages.contact,
            "resume": navbar_pages.resume,
            "certificates": navbar_pages.certificates,
            "about": navbar_pages.about,
        }