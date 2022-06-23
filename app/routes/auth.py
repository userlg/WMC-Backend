from xml.dom import NotSupportedErr
from flask import render_template, Blueprint, jsonify, make_response, request

from ..Models.models import User

from werkzeug.security import generate_password_hash

import uuid

auth_bp = Blueprint("auth_bp", __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    
    if request.method == 'POST':

        username = request.json['username']
        print(username)

        test_token = uuid.uuid4()

        response = make_response({ "message" : test_token})

        response.status_code = 201

        return response


@auth_bp.route('/signup', methods=['POST'])
async def signup():
    if request.method == 'POST':
        
        username = request.json['username']
        password = generate_password_hash(request.json['password'])

        user = User(username=username, password=password)

        try:
          await user.save()
          response = make_response({ "message": "User created correctly"})
          response.status_code = 201
          return response

        except Exception as e:
          print(e)
          response = make_response({ "message": "The username already exist"})
          response.status_code = 400
          return response

      
    
