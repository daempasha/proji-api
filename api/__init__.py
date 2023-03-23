"""Entry point into the application"""

import os
from flask import Flask, jsonify
from flask_cors import CORS

from .auth import require_auth

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
    cors.init_app(app, resources={r"/api/*": {"origins": app.config["FRONTEND_HOST"]}})

    @app.route("/")
    def hello():
        return "Hello world"

    @app.route("/api/test")
    def apitest():
        return {"data": "Test API"}

    @app.route("/api/public")
    def public():
        """No access token required."""
        response = (
            "Hello from a public endpoint! You don't need to be"
            " authenticated to see this."
        )
        return jsonify(message=response)

    @app.route("/api/private")
    @require_auth(None)
    def private():
        """A valid access token is required."""
        response = (
            "Hello from a private endpoint! You need to be"
            " authenticated to see this."
        )
        return jsonify(message=response)

    @app.route("/api/private-scoped")
    @require_auth("read:messages")
    def private_scoped():
        """A valid access token and scope are required."""
        response = (
            "Hello from a private endpoint! You need to be"
            " authenticated and have a scope of read:messages to see"
            " this."
        )
        return jsonify(message=response)

    return app
