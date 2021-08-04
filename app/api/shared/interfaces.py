from mypy_extensions import TypedDict


class TechnologyInterface(TypedDict, total=False):
    name: str
    description: str


class PlatformInterface(TypedDict, total=False):
    name: str
    description: str


class IMGInfoInterface(TypedDict, total=False):
    cloud_path: str
    alt: str
