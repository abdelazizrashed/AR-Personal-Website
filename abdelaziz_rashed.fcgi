from flup.server.fcgi import WSGIServer
from app.frontend import create_app as creat_frontend_app
from app.api import create_app as create_api_app
from subdomain_dispatcher import SubdomainDispatcher


app = SubdomainDispatcher("localhost", create_api_app, creat_frontend_app, None)

if __name__ == "__main__":
    WSGIServer(app).run()