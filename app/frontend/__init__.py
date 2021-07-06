import os
from flask import Flask, render_template, request
import jinja2

app = Flask(__name__)

loader = jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), "templates"))

enviroment = jinja2.Environment(loader=loader)


nav = [
    {"name": "Home", "url": "/"},
    {"name": "Projects", "url": "/projects"},
    {"name": "Services", "url": "/services"},
    {"name": "Contact", "url": "/contact"},
    {"name": "Resume", "url": "/resume"},
    {"name": "Certificates", "url": "/certificates"},
    {"name": "About", "url": "/about"},
]


@app.route("/")
def home():
    return render_template(
        "pages/index.html",
        nav=nav,
        title="Abdelaziz Rashed Personal Website",
        url="/",
        description="Abdelaziz Rashed is a software developer with wide skill set and experience in Web Development, Cross-platform App Development and Game Development.",
    )


@app.route("/projects")
def projects():
    return render_template(
        "pages/projects.html",
        nav=nav,
        title="Projects",
        url="/projects",
        description="Projects that Abdelaziz Rashed worked on in the past.",
    )


@app.route("/services")
def services():
    return render_template(
        "pages/services.html",
        nav=nav,
        title="Services",
        url="/services",
        description="Services that Abdelaziz Rashed provide.",
    )


@app.route("/contact")
def contact():
    return render_template(
        "pages/contact.html",
        nav=nav,
        title="Contact Abdelaziz Rashed",
        url="/contact",
        description="Ways you can contact Abdelaziz Rashed for future work.",
    )


@app.route("/resume")
def resume():
    return render_template(
        "pages/resume.html",
        nav=nav,
        title="Abdelaziz Rashed's resume",
        url="/resume",
        description="The resume of Abdelaziz Rashed",
    )


@app.route("/certificates")
def certificates():
    return render_template(
        "pages/certificates.html",
        nav=nav,
        title="Abdelaziz Rashed's certificates",
        url="/certificates",
        description="Certificates that Abdelaziz Rashed acquired through his career.",
    )


@app.route("/about")
def about():
    return render_template(
        "pages/about.html",
        nav=nav,
        title="About Abdelaziz Rashed",
        url="/about",
        description="Learn more about Abdelaziz Rashed and know who he is.",
    )


@app.route("/project")
def project():
    """
    request formate /project?id=1&name=new-project
    """
    project_id = request.args.get("id", default=1, type=int)
    project_name = request.args.get("name", default="", type=str)
    return render_template(
        "pages/project.html",
        nav=nav,
        title=project_name,
        url="/project",
        description="Information about the project "
        + project_name
        + " that Abdelziz Rashed worked on.",
    )


@app.route("/service")
def service():
    """
    request formate /service?id=1&name=new-service
    """
    service_id = request.args.get("id", default=1, type=int)
    service_name = request.args.get("name", default="", type=str)
    return render_template(
        "pages/service.html",
        nav=nav,
        title=service_name,
        url="/service",
        description="Information about the service "
        + service_name
        + " that Abdelziz Rashed provide.",
    )


@app.route("/certificate")
def certificate():
    """
    request formate /certifcate?id=1&name=new-certificate
    """
    certificate_id = request.args.get("id", default=1, type=int)
    certificate_name = request.args.get("name", default="", type=str)
    return render_template(
        "pages/certificate.html",
        nav=nav,
        title=certificate_name,
        url="/certificate",
        description="Information about the certificate "
        + certificate_name
        + " that Abdelziz acquired.",
    )
