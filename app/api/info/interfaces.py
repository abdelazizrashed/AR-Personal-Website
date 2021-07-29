from mypy_extensions import TypedDict


class IMGInfoInterface(TypedDict, total=False):
    cloud_path: str
    alt: str


class NavbarPagesInterface(TypedDict, total=False):

    home: bool
    projects: bool
    services: bool
    contact: bool
    resume: bool
    certificates: bool
    about: bool


class InfoInterface(TypedDict, total=False):

    navbar_pages: NavbarPagesInterface
    home_page_intro: str
    home_laptop_img_info: IMGInfoInterface
    home_tablet_img_info: IMGInfoInterface
    home_phone_img_info: IMGInfoInterface
    ar_about_pic_cloud_path: str
    ar_about_long_parag: str
    ar_about_short_parag: str
    ar_email: str
    ar_phone_no: str
