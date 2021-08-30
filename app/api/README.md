API which is responsible of controlling the api requests routes and the database (api stuff). It is divided into modules, each module is responsible of a certain functionality and hence has its out route. Everything is pretty standard across the app. Every script does the same thing as other scripts with the same name and they are templates with the logic is different.

<----Modules---->

auth => Controls the users CRUD operations to the db as well as authentication like logging in/ logging out.
certificates => deprecated
config => contains the config files of the app. It contains app parameters, api key, and any info used across the app. Check __init__.py create_app() to know how it's used.
info => This module contains general info that is displayed on the website like paragraphs, photos, navbar displayed pages, and any other info that we only need one of it.
projects => This module controls the projects data (projects are previous work or demos) CRUD operations to the db as well as the routes.
services => Services that we can provide (You got the idea of what it does)
Shared => This module joins things that are not specific to a specific module but are used across all.

<----Scripts---->
__init__.py => is responsible of creating the app and configure it\
blueprints.py => contains the method attach_blueprints() which attach the app blueprints to a given instance of the api app
custom_blueprint.py => Create a custom class inherited from the flask Blueprint class that add additional info to the blueprint
firebase_controller.py => useless