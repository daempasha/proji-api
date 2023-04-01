"""Import all routes and export a function to register all the blueprints."""

from flask import Flask
from .boards import blueprint as boards_blueprint

routes = [boards_blueprint]


def register_blueprints(app: Flask):
    """Go through each route and register the blueprint."""
    for route in routes:
        app.register_blueprint(route)
