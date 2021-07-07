from .interfaces import InfoInterface, NavbarPagesInterface


class InfoModel:

    navbar_pages: NavbarPagesModel
    home_page_intro: str
    home_laptop_img_url: str
    home_tablet_img_url: str
    home_phone_img_url: str
    abdelaziz_rashed_about_pic_url: str
    abdelaziz_rashed_about_long_parag: str
    abdelaziz_rashed_about_short_parag: str
    abdelaziz_rashed_email: str
    abdelaziz_rashed_phone_no: str

    def update(self, changes: InfoInterface):
        for key, value in changes.items():
            if key == "navbar_pages":
                pages = NavbarPagesModel()
                pages.update(value)
                setattr(self, key, pages)
            else:
                setattr(self, key, value)


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