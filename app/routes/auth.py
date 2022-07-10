from flask import Blueprint

from ..libs.auth_controllers import controllers_login, controllers_signup

auth_bp = Blueprint("auth_bp", __name__)


@auth_bp.route("/login", methods=["POST"])
def login():
    return controllers_login()


@auth_bp.route("/signup", methods=["POST"])
def signup():
    return controllers_signup()

@auth_bp.route("/logout", methods=["GET"])
def logout():
    return "logout"