auth module (to know what it does check api README.md). Everything is pretty standard across the app

<----Scripts---->
__init__.py => Adds the flask_restful resources to the blueprint.
controller.py => Creates the blueprint of the module and the api as well as some objects that are used across the app
models.py => Defines the data objects that are used to store the data.
interfaces.py => Defines a custom dictionary of the data model that define its fields.
services.py => Contains the logic of each model.
resources.py => Contains the flask_restful resource. Each resource is mapped to a route.
schemas.py => It was intended to be used to convert models from and to json but I used methods json() and from_json() in model services instead.