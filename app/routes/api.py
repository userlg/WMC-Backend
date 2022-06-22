from flask import render_template, Blueprint, jsonify, make_response

api_bp = Blueprint("api_bp", __name__)

@api_bp.route('/', methods=['GET'])
def home():
    return "<h3> Welcome to this app </h3>"




'''
from flask import render_template, Blueprint, jsonify, make_response
from ..models.users import User

views_bp = Blueprint("views_bp", __name__)


@views_bp.route('/',methods=['GET'])
def index():

    #number = randint(1,10)

    return render_template('index.html')



@views_bp.route('/all_users',methods=['GET'])
def all_users():
    result = User.objects.all()
    response = make_response({"Operation":"Successfull","users":result})
    return jsonify(result),200
'''