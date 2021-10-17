from app.api.projects.services import ProjectServices
from .controller import api
from .resources import ProjectResources, ProjectsResources


api.add_resource(ProjectResources, "/projects/project")
api.add_resource(ProjectServices, "/projects/projects")