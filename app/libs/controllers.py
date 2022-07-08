# ----------This file is only to general settings controllers

from flask import request, current_app as app, make_response, Response

from werkzeug.utils import secure_filename

import uuid

import os

ALLOWED_EXTENSIONS_VIDEOS = {"mp4", "mkv"}

ALLOWED_EXTENSIONS_PHOTOS = {"jpg", "jpeg", "png"}


# ------------Midlewares----------------
def allowed_file_vids(filename):
    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS_VIDEOS
    )


def allowed_file_photos(filename):
    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS_PHOTOS
    )


# --------------------------------------


# ---------Controllers


# --------Controller to handler the photos file upload process
def controllers_upload_videos() -> Response:
    if request.method == "POST":
        new_name = str(uuid.uuid4()) + ".mp4"
        if "video" not in request.files:
            response = make_response({"message": "Request dont has any file"})
            response.status_code = 406
            return response
        file = request.files["video"]
        if file.filename == "":
            response = make_response({"message": "File dont has a name"})
            response.status_code = 406
            return response
        if file and allowed_file_vids(file.filename):
            original_name = secure_filename(file.filename)
            new_name_file = secure_filename(str(new_name))
            file.save(os.path.join(app.config["UPLOAD_FOLDER"], new_name_file))
            response = make_response(
                {"message": "File saved successfully", "new_file": new_name_file}
            )
            response.status_code = 201
            return response
        else:
            response = make_response({"message": "Incorrect file"})
            response.status_code = 406
            return response


# --------Controller to handler the photos file upload process
def controllers_upload_photos() -> Response:
    if request.method == "POST":
        new_name = str(uuid.uuid4()) + ".png"
        if "photo" not in request.files:
            response = make_response({"message": "Request dont has any file"})
            response.status_code = 406
            return response
        file = request.files["photo"]
        if file.filename == "":
            response = make_response({"message": "File dont has a name"})
            response.status_code = 406
            return response
        if file and allowed_file_photos(file.filename):
            original_name = secure_filename(file.filename)
            new_name_file = secure_filename(str(new_name))
            file.save(os.path.join(app.config["UPLOAD_FOLDER"], new_name_file))
            response = make_response(
                {"message": "File saved successfully", "new_file": new_name_file}
            )
            response.status_code = 201
            return response
        else:
            response = make_response({"message": "Incorrect file"})
            response.status_code = 406
            return response
