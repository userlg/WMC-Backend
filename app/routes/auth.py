from flask import render_template, Blueprint, jsonify, make_response

auth_bp = Blueprint("auth_bp", __name__)

@auth_bp.route('/login', methods=['GET'])
def login():
    return "<h3> Welcome to this Login View </h3>"
