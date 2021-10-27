from flask import current_app as app, request
from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required

from app.api.shared.helpers.services import HelperServices
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
        "homeLaptopImgInfo",
        type=dict,
        help="An image that will be displayed inside the laptop screen on the home page",
    )
    _info_parser.add_argument(
        "homeTabletImgInfo",
        type=dict,
        help="An image that will be displayed inside the tablet screen on the home page",
    )
    _info_parser.add_argument(
        "homePhoneImgInfo",
        type=dict,
        help="An image that will be displayed inside the phone screen on the home page",
    )
    _info_parser.add_argument(
        "A_RashedAboutPicInfo",
        type=dict,
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
        data = self._info_parser.parse_args()
        files, datas = HelperServices.seperate_files_and_json_data(request, HelperServices.ALLOWED_IMG_EXTENSIONS, ["img"], ["data"])
        data = datas["data"]
        
        attrs = dict(data)
        info_object = InfoServices.create(attrs, app)
        if info_object:
            return {
                "message": "Data created successfully",
                "Info": InfoServices.json(info_object, app),
            }, 201
        # try:
        # except:
        #     return {
        #         "description": "Internal server error",
        #         "error": "internal_server_error",
        #     }, 500

    @jwt_required(fresh=True)
    def put(self):
        data = self._info_parser.parse_args()

        attrs = dict(data)

        info_object = InfoServices.update(attrs, app)
        if info_object:
            return {
                "message": "Data updated successfully",
                "Info": InfoServices.json(info_object, app),
            }, 200
        else:
            return {
                "description": "Error in updating info",
                "error": "internal_server_error",
            }, 500

        # try:
        # except:
        #     return {
        #         "description": "Internal server error",
        #         "error": "internal_server_error",
        #     }, 500

    def get(self):
        info = InfoServices.retrieve(app)
        return InfoServices.json(info, app)

    # try:
    # except:
    #     return {
    #         "description": "Internal server error",
    #         "error": "internal_server_error",
    #     }, 500
