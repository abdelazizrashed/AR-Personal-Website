from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask.json import jsonify
from app.api.shared.db_man.services import db
from app.api.shared.jwt.models import TokenBlocklistModel
from .auth.models import UserModel
from .auth.services import UserServices
import os


def create_app(domain=""):

    from .blueprints import attach_blueprints

    app = Flask(__name__)
    CORS(app)
    app.config.from_pyfile(os.path.join(os.path.dirname(__file__), "config/dev.config"))
    try:
        app.config.from_envvar("APPLICATION_CONFIG_FILE")
    except:
        pass
        # if domain == "localhost":
        #     app.config["DOMAIN"] = domain + ":5000"
        # else:
    app.config["DOMAIN"] = domain

    jwt = JWTManager(app)

    db.app = app
    db.init_app(app)
    db.create_all()

    attach_blueprints(app)

    @jwt.additional_claims_loader
    def add_claims_to_jwt(identity):
        """
        This method is used to attach the information of the user to the JWT access token.
        """
        user = UserServices.retrieve_by_user_id(identity, app)
        if user:
            return {
                "user_id": user.user_id,
                "username": user.username,
                "email": user.email,
            }
        return {"description": "User is not logged in", "error": "not_logged_in"}, 401

    @jwt.token_in_blocklist_loader  # callback to chick if the jwt exists in the jwt blocklist database
    def check_if_token_revoked(jwt_header, jwt_payload):
        jti = jwt_payload["jti"]
        token = db.session.query(TokenBlocklistModel.id).filter_by(jti=jti).scalar()
        return token is not None

    @jwt.expired_token_loader  # going to be called when the toke expires
    def expired_token_callback(jwt_header, jwt_payload):
        return (
            jsonify({"description": "The token has expired", "error": "token_expired"}),
            401,
        )

    @jwt.invalid_token_loader  # going to be called when the authentication is not jwt for example auth using jwt instead of Bearer when using flask_jwt_extended
    def invalid_token_callback(error):
        return jsonify({"description": error, "error": "invalid_token"}), 401

    @jwt.unauthorized_loader  # going to be called when they don't send us a jwt at all
    def missing_token_callback(reason):
        return jsonify({"description": reason, "error": "authorization_required"}), 401

    @jwt.needs_fresh_token_loader  # going to be called when the token is not fresh and a fresh one is needed
    def token_not_fresh_callback(jwt_header, jwt_payload):
        return (
            jsonify(
                {
                    "description": "The token is not fresh",
                    "error": "fresh_token_required",
                }
            ),
            401,
        )

    @jwt.revoked_token_loader  # the toke has been revoked for example if the user is logged out
    def revoked_token_callback(jwt_header, jwt_payload):
        return (
            jsonify(
                {"description": "The token has been revoked", "error": "token_revoked"}
            ),
            401,
        )

    return app
