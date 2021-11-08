


from flask_restful import reqparse


_service_parser = reqparse.RequestParser()
_service_parser.add_argument("id", type=str)
_service_parser.add_argument("name", type=str)
_service_parser.add_argument("description", type=str)
_service_parser.add_argument("projectsIds", type=str)
_service_parser.add_argument("", type=str)