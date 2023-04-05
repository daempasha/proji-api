"""Get boards for users."""

from flask import Blueprint, Response, request
from datetime import datetime
from bson import json_util
from api import mongo
from api.auth import require_auth
from api.utils import get_user_info, extract_access_token

blueprint = Blueprint("boards", __name__, url_prefix="/api/boards")


@blueprint.route("", methods=["GET", "POST"])
@require_auth(None)
def boards():
    """Handle boards."""

    access_token = extract_access_token()
    user_info = get_user_info(access_token)

    if request.method == "GET":
        # Get all available boards.
        return Response(
            json_util.dumps(
                {"data": list(mongo.db.boards.find({"createdBy": user_info["email"]}))}
            ),
            mimetype="application/json",
        )

    if request.method == "POST":
        # Create a new board
        body = request.get_json()
        current_timestamp = datetime.utcnow()

        board_data = {
            **body,
            "createdBy": user_info["email"],
            "dateCreated": current_timestamp,
            "lastUpdated": current_timestamp,
        }

        mongo.db.boards.insert_one(board_data)

        return Response({"message": "Successfully added board!"})

    return Response({"message": "No method specified"}, 500)
