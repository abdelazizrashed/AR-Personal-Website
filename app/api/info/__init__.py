from .controller import api
from .resources import InfoResource

api.add_resource(InfoResource, "/info")
