from flask import Flask


def attach_blueprints(app: Flask):
    from app.api.info import info_blueprint
    from app.api.auth import auth_blueprint
    from app.api.certificates import certificates_blueprint
    from app.api.projects import projects_blueprint
    from app.api.services import services_blueprint

    app.register_blueprint(info_blueprint)
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(certificates_blueprint)
    app.register_blueprint(projects_blueprint)
    app.register_blueprint(services_blueprint)