from typing import List
from app.api.shared.models import PlatformModel, TechnologyModel, IMGInfoModel


class YouTubeVidModel:

    src: str
    title: str


class DetailModel:

    name: str
    description: str


class ProjectModel:

    name: str
    id_: str
    platforms_ids: List[str]
    technologies_ids: List[str]
    img_url: str
    description: str
    github_url: str
    app_store_url: str
    google_play_store_url: str
    website_url: str
    youtube_vid: YouTubeVidModel
    services_ids: List[str]
    imgs: List[IMGInfoModel]
    related_projects_ids: List[str]
    detailed_services: List[DetailModel]
    detailed_technologies: List[DetailModel]
    detailed_platforms: List[DetailModel]







