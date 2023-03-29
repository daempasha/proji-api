"""Entry point into the application"""

from flask import Flask, Response
from flask_cors import CORS
from flask_pymongo import PyMongo
from bson import json_util

from .auth import require_auth
from .error_handlers import register_error_handlers
from .utils import get_config_path

cors = CORS()
mongo = PyMongo()


def create_app():
    """
    Create and configure a Flask application instance.
    """
    app = Flask(__name__)

    config = get_config_path(app)
    app.config.from_object(config)

    cors.init_app(app, resources={r"/api/*": {"origins": app.config["FRONTEND_HOST"]}})
    mongo.init_app(app)

    online_users = mongo.db.boards.find()
    for user in online_users:
        print(user)

    register_error_handlers(app)

    @app.route("/api/boards", methods=["GET"])
    def get_boards():
        return Response(
            json_util.dumps({"data": list(mongo.db.boards.find())}),
            mimetype="application/json",
        )

    @app.route("/api/test")
    def apitest():
        return {"data": "Test API"}

    @app.route("/api/public")
    def public():
        """No access token required."""
        response = "Hello from a public endpoint! You don't need to be authenticated to see this."
        return Response(json_util.dumps({"data": response}))

    @app.route("/api/private")
    @require_auth(None)
    def private():
        """A valid access token is required."""
        response = (
            "Hello from a private endpoint! You need to be"
            " authenticated to see this."
        )
        return Response(json_util.dumps({"data": response}))

    @app.route("/api/private-scoped")
    @require_auth("read:messages")
    def private_scoped():
        """A valid access token and scope are required."""
        response = (
            "Hello from a private endpoint! You need to be"
            " authenticated and have a scope of read:messages to see"
            " this."
        )
        return Response(json_util.dumps({"data": response}))

    return app
