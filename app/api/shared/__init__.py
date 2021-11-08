from .controller import api
from .resources import (
    PlatformResource,
    PlatformsResource,
    TechnologiesResource,
    TechnologyResource, 
    ImageResource
)

api.add_resource(TechnologiesResource, "/shared/technologies") 
api.add_resource(TechnologyResource, "/shared/technology") 
api.add_resource(PlatformsResource, "/shared/platforms") 
api.add_resource(PlatformResource, "/shared/platform") 
api.add_resource(ImageResource, "/shared/image")
