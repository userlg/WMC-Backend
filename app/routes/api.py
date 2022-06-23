from flask import render_template, Blueprint, jsonify, make_response

from ..Models.models import User

import random

names = ['Laura','Jose','Juan','Megas','Star','FireXone','Manche','Julian','Zero','Asterix']

api_bp = Blueprint("api_bp", __name__)

@api_bp.route('/', methods=['GET'])
def home():
    random_number = random.randint(1,1001)

    username = random.choice(names) + str(random_number)

    year = random.randint(1980,2002)

    return "Hello flask"