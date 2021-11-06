from .controller import api
from .resources import ProjectResources, ProjectsResources


api.add_resource(ProjectResources, "/projects/project")
api.add_resource(ProjectsResources, "/projects/projects")