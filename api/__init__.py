"""Entry point into the application"""

import os
from flask import Flask
from flask_cors import CORS

cors = CORS()


def create_app():
    """
    Create and configure a Flask application instance.
    """
    app = Flask(__name__)

    debug = app.config["DEBUG"]
    testing = os.environ.get("TESTING", default="0") == "1"

    if testing:
        config = "api.config.Testing"
    elif debug:
        config = "api.config.Development"
    else:
        config = "api.config.Production"

    app.config.from_object(config)
    cors.init_app(app, origins=[app.config["FRONTEND_HOST"]])

    @app.route("/")
    def hello():
        return "Hello world"

    @app.route("/api/test")
    def apitest():
        return {"data": "Test API"}

    return app
