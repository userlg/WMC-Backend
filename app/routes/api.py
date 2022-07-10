from flask import (
    Blueprint,
)

from ..Models.models import User

from ..libs.controllers import controllers_upload_videos, controllers_upload_photos

api_bp = Blueprint("api_bp", __name__)


@api_bp.route("/", methods=["GET"])
def home():
    # This part is reserve to he home main view
    return "Hello flask"


@api_bp.route("/about", methods=["GET"])
def about():
    return "About Route"


@api_bp.route("/uploads_videos", methods=["POST"])
def uploads_videos():
    return controllers_upload_videos()


@api_bp.route("/uploads_photos", methods=["POST"])
def uploads_photos():
    return controllers_upload_photos()


@api_bp.errorhandler(404)
def page_not_found(error):
    print(error)
    return "Resource does not exist", 404
