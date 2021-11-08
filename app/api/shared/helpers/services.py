from gcloud import storage
import pyrebase
from flask import Flask, Request
from werkzeug.datastructures import FileStorage
from typing import List, Tuple, Dict
import json
from werkzeug.security import safe_str_cmp
import copy
from distutils.util import strtobool

def any2bool(sm) -> bool:
    return bool(strtobool(sm))


class HelperServices:


    ALLOWED_IMG_EXTENSIONS = ["png", "jpg", "jpeg"]

    @staticmethod
    def check_if_file_exists(cloud_path: str, app: Flask)-> bool:
        storage = HelperServices.get_firebase_storage(app)
        return storage.bucket.blob(cloud_path).exists()

    @staticmethod
    def get_url_from_cloud_path(cloud_path: str, firebase_storage: pyrebase.pyrebase.Storage) -> str:
        if cloud_path:
            return firebase_storage.child(cloud_path).get_url(None)
        return None

    @staticmethod
    def upload_file(file: FileStorage, app: Flask, cloud_path: str = None) -> str:
        """
        Upload file to the data base and return the cloud_path.
        """
        storage = HelperServices.get_firebase_storage(app)
        if not cloud_path:
            db = HelperServices.get_firebase_database(app)
            cloud_path = "images/"
            img_key = db.generate_key()
            cloud_path = f"images/{img_key}.jpg"
            storage.child(cloud_path).put(file)
            return cloud_path
        storage.child(cloud_path).put(file)
        return cloud_path

    @staticmethod
    def delete_file(cloud_path: str, app: Flask) -> str:
        storage = HelperServices.get_firebase_storage(app)
        storage.child(cloud_path).delete()
        return cloud_path
        
    # @staticmethod
    # def update_file(cloud_path: str, app: Flask) -> str:


    @staticmethod
    def get_firebase_object(app: Flask) -> pyrebase.pyrebase.Firebase:
        return pyrebase.initialize_app(app.config["FIREBASE_CONFIG"])

    @staticmethod
    def get_firebase_database(app: Flask) -> pyrebase.pyrebase.Database:
        firebase = HelperServices.get_firebase_object(app)
        return firebase.database()

    @staticmethod
    def get_firebase_storage(app: Flask) -> pyrebase.pyrebase.Storage:
        firebase = HelperServices.get_firebase_object(app)
        return firebase.storage()
    
    @staticmethod
    def seperate_files_and_json_data(
        request: Request, 
        allowed_extensions: List[str] = ALLOWED_IMG_EXTENSIONS, 
        files_keys: List[str] = [], 
        json_keys: List[str] = []
        ) -> Tuple[Dict[str, List[FileStorage]], Dict[str, dict]]:
        files = dict()
        json_dicts = dict()
        for key in files_keys:
            files[key] = []
            fs = request.files[key].getlist()
            for f in fs:
                if HelperServices.allowed_file(f.filename, allowed_extensions):
                    files[key].append(f)
        for key in json_keys:
            l = request.form.getlist(key)
            json_dicts[key] = json.load(l[0])
        return (files, json_dicts)


    @staticmethod
    def allowed_file(filename: str, allowed_extensions: List[str]):
        return '.' in filename and \
            filename.rsplit('.', 1)[1].lower() in allowed_extensions

    @staticmethod
    def combine_imgs_and_dicts(imgs: List[FileStorage], dicts: List[dict]) -> List[dict]:
        imgs_dicts = copy.deepcopy(dicts)
        for img in imgs:
            for index in range(len(imgs_dicts)):
                if safe_str_cmp(img.filename, imgs_dicts[index].get("name")):
                    imgs_dicts[index][img] = img
        return imgs_dicts

    
