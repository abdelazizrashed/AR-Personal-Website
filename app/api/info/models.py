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

    navbar_pages: NavbarPagesModel
    home_page_intro: str
    home_laptop_img_info: IMGInfoModel
    home_tablet_img_info: IMGInfoModel
    home_phone_img_info: IMGInfoModel
    ar_about_pic_cloud_path: IMGInfoModel
    ar_about_long_parag: str
    ar_about_short_parag: str
    ar_email: str
    ar_phone_no: str

    def update(self, changes: InfoInterface):
        for key, value in changes.items():
            if key == "navbar_pages":
                pages = NavbarPagesModel()
                pages.update(value)
                setattr(self, key, pages)
            else:
                setattr(self, key, value)
        return self