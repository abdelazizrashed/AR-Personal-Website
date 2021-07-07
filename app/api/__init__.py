from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from flask.json import jsonify
from app.api.shared.db_man.services import db
from app.api.shared.jwt.models import TokenBlocklistModel


def create_app():

    from .blueprints import attach_blueprints

    app = Flask(__name__)
    app.config.from_pyfile("/config/dev.config")
    app.config.from_envvar("APPLICATION_CONFIG_FILE")

    api = Api(app)

    jwt = JWTManager(app)

    db.app = app
    db.init_app(app)
    db.create_all()

    attach_blueprints(app)

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
