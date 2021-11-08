from .interfaces import ServiceInterface, ServiceContentInterface
from typing import Dict, List
from app.api.shared.interfaces import IMGInfoInterface, TechnologyInterface


class ServiceContentModel:

    title: str
    paragraph: str

    def update(self, changes: ServiceContentInterface):
        for key, value in changes.items():
            setattr(self, key, value)
        return self

class ServiceTechnologyModel:
    name: str
    description: str


class ServiceModel:
    name: str
    description: str
    id_: str
    importance: int
    logo: IMGInfoInterface
    projects_ids: List[str]
    other_services_ids: List[str]
    content: List[ServiceContentModel]
    technologies: List[ServiceTechnologyModel]

    # def update(self, changes: ServiceInterface):
    #     for key, value in changes.items():
    #         setattr(self, key, value)
    #     return self
