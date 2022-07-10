from flask import Blueprint, make_response, request

from flask_jwt_extended import (
    create_access_token,
    get_jwt_identity,
    jwt_required,
    JWTManager,
)

from werkzeug.security import generate_password_hash, check_password_hash

from ..Models.models import User

from datetime import datetime as dt

import asyncio

import uuid

auth_bp = Blueprint("auth_bp", __name__)


@auth_bp.route("/login", methods=["POST"])
async def login():

    if request.method == "POST":

        username = request.json["username"]
        password = request.json["password"]
        try:
            user = User.objects(username=username).get_or_404()
        except Exception as e:
            # print(e)
            response = make_response({"message": "Some Data is incorrect"})
            response.status_code = 401
            return response

        if user:
            if check_password_hash(user["password"], password):
                access_token = create_access_token(identity=username)
                response = make_response(
                    {
                        "message": "Login process successfully",
                        "datetime": dt.now(),
                        "secure_token": access_token,
                    }
                )
                response.status_code = 200
                return response
            else:
                # -----Here the password is incorrect
                response = make_response({"message": "Some Data is incorrect"})
                response.status_code = 401
                return response


@auth_bp.route("/signup", methods=["POST"])
async def signup():
    if request.method == "POST":

        username = request.json["username"]
        password = generate_password_hash(request.json["password"])

        print(username + "||" + password)

        user = User(username=username, password=password)

        try:
            user.save()
            response = make_response({"message": "User created correctly"})
            response.status_code = 201
            return response

        except Exception as e:
            print(e)
            response = make_response({"message": "The username already exist"})
            response.status_code = 400
            return response
