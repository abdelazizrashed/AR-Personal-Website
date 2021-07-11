from app.frontend import create_app as creat_frontend_app
from app.api import create_app as create_api_app
from subdomain_dispatcher import SubdomainDispatcher
from waitress import serve


app = SubdomainDispatcher("localhost", create_api_app, creat_frontend_app, None)

serve(app, port=5000, host="0.0.0.0", threads=1)
