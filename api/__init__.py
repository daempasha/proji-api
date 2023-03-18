"""Entry point into the application"""

from flask import Flask


def create_app():
    """
    Create and configure a Flask application instance.
    """
    app = Flask(__name__)

    return app
