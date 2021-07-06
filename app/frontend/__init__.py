import os
from flask import Flask, render_template
import jinja2

app = Flask(__name__)

loader = jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), "templates"))

enviroment = jinja2.Environment(loader=loader)


@app.route("/")
def home():
    nav = [
        {"name": "Home", "url": "/"},
        {"name": "Projects", "url": "/projects"},
        {"name": "Services", "url": "/services"},
        {"name": "Contact", "url": "/contact"},
        {"name": "Resume", "url": "/resume"},
        {"name": "Certificates", "url": "/certificates"},
        {"name": "About", "url": "/about"},
    ]
    return render_template(
        "pages/index.html",
        nav=nav,
        title="Abdelaziz Rashed Personal Website",
        url = '/',
        description="Abdelaziz Rashed is a software developer with wide skill set and experience in Web Development, Cross-platform App Development and Game Development",
    )
