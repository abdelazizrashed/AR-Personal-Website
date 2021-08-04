from .interfaces import IMGInfoInterface, TechnologyInterface, PlatformInterface


class IMGInfoModel:
    cloud_path: str
    alt: str

    def update(self, changes: IMGInfoInterface):
        for key, value in changes.items():
            setattr(self, key, value)
        return self


class TechnologyModel:
    name: str
    description: str

    def update(self, changes: TechnologyInterface):
        for key, value in changes.items():
            setattr(self, key, value)
        return self


class PlatformModel:
    name: str
    description: str

    def update(self, changes: TechnologyInterface):
        for key, value in changes.items():
            setattr(self, key, value)
        return self