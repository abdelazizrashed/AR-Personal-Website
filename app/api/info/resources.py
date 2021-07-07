from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required
from .interfaces import InfoInterface, NavbarPagesInterface
from .models import InfoModel, NavbarPagesModel
from .services import InfoServices, NavbarPageServices


class InfoResource(Resource):

    _info_parser = reqparse.RequestParser()

    _info_parser.add_argument(
        "navbarPages",
        type=dict,
        help="A json object that include which pages to be display and what not",
    )
    _info_parser.add_argument(
        "homePageIntro",
        type=str,
        help="A string that will be displayed under the navbar in the home page",
    )
    _info_parser.add_argument(
        "homeLaptopImgCloudPath",
        type=str,
        help="An image that will be displayed inside the laptop screen on the home page",
    )
    _info_parser.add_argument(
        "homeTabletImgCloudPath",
        type=str,
        help="An image that will be displayed inside the tablet screen on the home page",
    )
    _info_parser.add_argument(
        "homePhoneImgCloudPath",
        type=str,
        help="An image that will be displayed inside the phone screen on the home page",
    )
    _info_parser.add_argument(
        "A_RashedAboutPicCloudPath",
        type=str,
        help="Personal picture of Abdelaziz Rashed",
    )
    _info_parser.add_argument(
        "A_RashedAboutLongParag",
        type=str,
        help="A relativly long introduction paragraph about Abdelaziz Rashed",
    )
    _info_parser.add_argument(
        "A_RashedAboutShortParag",
        type=str,
        help="A short introduction paragraph about Abdelaziz Rashed",
    )
    _info_parser.add_argument(
        "A_RashedEmail",
        type=str,
        help="The email of Abdelaziz Rashed that is used to get in contact with him",
    )
    _info_parser.add_argument(
        "A_RashedPhoneNo", type=str, help="The phone number of Abdelaziz Rashed"
    )

    @jwt_required(fresh=True)
    def post(self):
        data = _info_parser.parse_args()

        attrs = dict(data)

        info_object = InfoServices.create(attrs)
        if info_object:
            return {
                "message": "Data created successfully",
                "Info": InfoServices.json(info_object),
            }, 201

    @jwt_required(fresh=True)
    def put(self):
        data = _info_parser.parse_args()

        attrs = dict(data)

        info_object = InfoServices.update(attrs)
        if info_object:
            return {
                "message": "Data created successfully",
                "Info": InfoServices.json(info_object),
            }, 200

    def get(self):
        info = InfoServices.get()
        return InfoServices.json(info)