"""Get boards for users."""

from flask import Blueprint, Response
from bson import json_util
from api import mongo

blueprint = Blueprint("boards", __name__, url_prefix="/api/boards")


@blueprint.route("")
def get_boards():
    """Get boards from Mongodb."""
    return Response(
        json_util.dumps({"data": list(mongo.db.boards.find())}),
        mimetype="application/json",
    )
