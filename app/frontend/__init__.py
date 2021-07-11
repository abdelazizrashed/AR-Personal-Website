import os
from flask import Flask, render_template, request

from .views import main


def create_app(domain=""):
    app = Flask(__name__)

    # if domain == "localhost":
    #     app.config["DOMAIN"] = domain + ":5000"
    # else:
    app.config["DOMAIN"] = domain

    app.register_blueprint(main)

    return app