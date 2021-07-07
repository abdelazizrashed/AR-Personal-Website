from mypy_extensions import TypedDict


class InfoInterface(TypedDict, total=false):

    navbar_pages: NavbarPagesInterface
    home_page_intro: str
    home_laptop_img_cloud_path: str
    home_tablet_img_cloud_path: str
    home_phone_img_cloud_path: str
    ar_about_pic_cloud_path: str
    ar_about_long_parag: str
    ar_about_short_parag: str
    ar_email: str
    ar_phone_no: str


class NavbarPagesInterface(TypedDict, total=false):

    home: bool
    projects: bool
    services: bool
    contact: bool
    resume: bool
    certificates: bool
    about: bool