from werkzeug.serving import run_simple
from app.frontend import create_app as creat_frontend_app
from app.api import create_app as create_api_app
from app import create_app


# app = SubdomainDispatcher("localhost", create_api_app, creat_frontend_app, None)
app = create_app("localhost:5000")

if __name__ == "__main__":
    run_simple(
        "0.0.0.0",
        5000,
        app,
        use_reloader=True,
        use_debugger=True,
        use_evalex=True,
        threaded=True,
    )