from .interfaces import InfoInterface, NavbarPagesInterface, IMGInfoInterface
from app.api.shared.models import IMGInfoModel


class NavbarPagesModel:

    home: bool = True
    projects: bool = True
    services: bool = True
    contact: bool
    resume: bool
    certificates: bool
    about: bool

    def update(self, changes: NavbarPagesInterface):
        for key, value in changes.items():
            if key == "home" or key == "projects" or key == "services":
                setattr(self, key, True)
            else:
                setattr(self, key, value)
        return self


class InfoModel:

    navbar_pages: NavbarPagesModel = None
    home_page_intro: str = None
    home_laptop_img_info: IMGInfoModel = None
    home_tablet_img_info: IMGInfoModel = None
    home_phone_img_info: IMGInfoModel = None
    ar_about_pic_info: IMGInfoModel = None
    ar_about_long_parag: str = None
    ar_about_short_parag: str = None
    ar_email: str = None
    ar_phone_no: str = None

    def update(self, changes: InfoInterface):
        for key, value in changes.items():
            if key == "navbar_pages":
                pages = NavbarPagesModel()
                pages.update(value)
                setattr(self, key, pages)
            else:
                setattr(self, key, value)
        return self