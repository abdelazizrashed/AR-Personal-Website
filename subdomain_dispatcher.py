from threading import Lock
from werkzeug.exceptions import abort


class SubdomainDispatcher(object):
    def __init__(
        self,
        domain,
        create_api_app,
        create_frontend_app,
        create_dashboard_app,
        debug=False,
    ):
        self.domain = domain
        self.api_app = None
        self.frontend_app = None
        self.dashboard_app = None
        if create_api_app:
            self.api_app = create_api_app(domain)
        if create_frontend_app:
            self.frontend_app = create_frontend_app(domain)
        if create_dashboard_app:
            self.dashboard_app = create_dashboard_app(domain)
        self.lock = Lock()
        self.instances = {
            "": self.frontend_app,
            "api": self.api_app,
            "dashboard": self.dashboard_app,
        }

    def get_application(self, host):
        host = host.split(":")[0]
        assert host.endswith(self.domain), "Configuration error"
        subdomain = host[: -len(self.domain)].rstrip(".")
        with self.lock:
            app = self.instances.get(subdomain)
            if app is None:
                abort(404)
            return app

    def __call__(self, environ, start_response):
        app = self.get_application(environ["HTTP_HOST"])
        return app(environ, start_response)