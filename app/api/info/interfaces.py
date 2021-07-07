from mypy_extensions import TypedDict


class InfoInterface(TypedDict, total=false):

    navbar_pages: NavbarPagesInterface
    home_page_intro: str
    home_laptop_img_url: str
    home_tablet_img_url: str
    home_phone_img_url: str
    abdelaziz_rashed_about_pic_url: str
    abdelaziz_rashed_about_long_parag: str
    abdelaziz_rashed_about_short_parag: str
    abdelaziz_rashed_email: str
    abdelaziz_rashed_phone_no: str


class NavbarPagesInterface(TypedDict, total=false):

    home: bool
    projects: bool
    services: bool
    contact: bool
    resume: bool
    certificates: bool
    about: bool