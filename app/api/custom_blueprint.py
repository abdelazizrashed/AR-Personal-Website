from flask import Blueprint
import pyrebase

firebase = None


class CustomBlueprint(Blueprint):
    def register(self, app, options, first_registration=False):
        global firebase

        config = app.config
        firebase_config = config.get("FIREBASE_CONFIG")

        firebase = pyrebase.initialize_app(firebase_config)

        super(CustomBlueprint, self).register(app, options, first_registration)
