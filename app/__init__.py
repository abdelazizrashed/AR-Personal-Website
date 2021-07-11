from werkzeug.middleware.dispatcher import DispatcherMiddleware
from .api import create_app as create_api_app
from .frontend import create_app as create_frontend_app

# from .dashboard import create_app as create_dashboard_app


def create_app(domain=""):

    api_app = create_api_app()
    frontend_app = create_frontend_app()
    # dashboard_app = create_dashboard_app

    app = DispatcherMiddleware(
        frontend_app,
        {
            "/api": api_app,
        },
    )

    return app