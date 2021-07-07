
class HelperServices:

    @staticmethod
    def get_url_from_cloud_path(cloud_path: str, firebase_storage):
        return firebase_storage.child(cloud_path).get_url()