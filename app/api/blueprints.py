from flask import Flask


def attach_blueprints(app: Flask):
    from app.api.info.controller import info_blueprint
    from app.api.auth.controller import auth_blueprint
    from app.api.certificates.controller import certificates_blueprint
    from app.api.projects.controller import projects_blueprint
    from app.api.services.controller import services_blueprint
    from app.api.shared.controller import shared_blueprint

    app.register_blueprint(info_blueprint)
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(certificates_blueprint)
    app.register_blueprint(projects_blueprint)
    app.register_blueprint(services_blueprint)
    app.register_blueprint(shared_blueprint)