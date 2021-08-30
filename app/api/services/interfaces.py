from typing import List, Dict
from mypy_extensions import TypedDict
from app.api.shared.interfaces import IMGInfoInterface, TechnologyInterface


class ServiceInterface(TypedDict, total=False):
    name: str
    description: str
    id: str
    importance: int
    logo: IMGInfoInterface
    projects: List[Dict]
    other_services: List[Dict]
    content: List[ServiceContentInterface]
    technologies: List[TechnologyInterface]


class ServiceContentInterface(TypedDict, total=False):
    title: str
    paragraph: str
