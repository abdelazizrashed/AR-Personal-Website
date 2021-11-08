from .controller import api

from .resources import ServiceResources, ServicesResources

api.add_resource(ServiceResources, "/services/service")
api.add_resource(ServicesResources, "/services/services")