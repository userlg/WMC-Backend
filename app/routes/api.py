from flask import (
    render_template,
    Blueprint,
    jsonify,
    make_response,
    request,
    redirect,
    flash,
    url_for,
    current_app as app,
)

from ..Models.models import User

from werkzeug.utils import secure_filename

import random

import os

import uuid

api_bp = Blueprint("api_bp", __name__)

ALLOWED_EXTENSIONS = {"mp4", "mkv"}


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@api_bp.route("/", methods=["GET"])
def home():
    #This part is reserve to he home main view

    return "Hello flask"


@api_bp.route("/about", methods=["GET"])
def about():
    return "About Route"


@api_bp.route("/uploads", methods=["POST"])
def uploads():
    if request.method == "POST":
        new_name = str(uuid.uuid4()) + '.mp4'
        # check if the post request has the file part
        print(request.files)
        if "video" not in request.files:
            response = make_response({"message": "Format file not allow"})
            response.status_code = 406
            return response
        file = request.files["video"]
        if file.filename == "":
            response = make_response({"message": "File dont has a name"})
            response.status_code = 406
            return response
        if file and allowed_file(file.filename):
            original_name = secure_filename(file.filename)
            new_name_file = secure_filename(str(new_name))
            file.save(os.path.join(app.config["UPLOAD_FOLDER"], new_name_file))
            response = make_response({"message": "File saved successfully"})
            response.status_code = 201
            return response