"""Get boards for users."""

from flask import Blueprint, Response, request
from bson import json_util
from api import mongo
from api.auth import require_auth

blueprint = Blueprint("boards", __name__, url_prefix="/api/boards")


@blueprint.route("", methods=["GET", "POST"])
@require_auth(None)
def boards():
    """Handle boards."""
    if request.method == "GET":
        # Get all available boards.
        return Response(
            json_util.dumps({"data": list(mongo.db.boards.find())}),
            mimetype="application/json",
        )

    if request.method == "POST":
        # Create a new board
        body = request.get_json()

        mongo.db.boards.insert_one(body)

        return {"message": "Successfully added board!"}
