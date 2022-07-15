from flask import Response, request, make_response

from werkzeug.security import generate_password_hash, check_password_hash

from ..Models.users import User

from ..Models.blacklist import Blacklist

from ..libs.resposes import generate_response, generate_response_jwt

from datetime import datetime as dt

from flask_jwt_extended import (
    create_access_token,
    get_jwt_identity,
    jwt_required,
    JWTManager,
)


# ---------Controllers to the signup of new users
def controllers_login():
    if request.method == "POST":
        username = request.json["username"]
        password = request.json["password"]
        try:
            user = User.objects(username=username).get_or_404()
        except Exception as e:
            message = "Some Data is incorrect"
            return generate_response(message,401)

        if user:
            if check_password_hash(user["password"], password):
                access_token = create_access_token(identity=username)
                message = "Login process successfully"
                return generate_response_jwt(message,access_token,200)
            else:
                # -----Here the password is incorrect
                message = "Some Data is incorrect"
                return generate_response(message,401)

# ---------Controllers to the signup of nwe users
def controllers_signup() -> Response:
    if request.method == "POST":
        username = request.json["username"]
        password = request.json["password"]

        if len(username) < 6 or len(password) < 6:
                message = "username and password must be at least 6 characters long"
                return generate_response(message,401)

        user = User(username=username, password=generate_password_hash(password))

        try:
            user.save()
            message ="User created correctly"
            return generate_response(message,201)

        except Exception as e:
            print(e)
            message = "The username already exist"
            return  generate_response(message,401)
