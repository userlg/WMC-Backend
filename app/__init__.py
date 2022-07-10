# --------Imports Segments-----------------
from flask import Flask

from flask_cors import CORS

from flask_mongoengine import MongoEngine

from flask_socketio import SocketIO

from flask_jwt_extended import (
    create_access_token,
    get_jwt_identity,
    jwt_required,
    JWTManager,
)

from .routes.api import api_bp

from .routes.auth import auth_bp

from .config.config import Production, Development

from .libs.modules import get_port, get_host

import os

# ----------End Imports Segments------------


###------Function to Create the main app
def create_app() -> Flask:
    app = Flask(__name__)
    # Settings app
    # app.config.from_object(Production())
    app.config.from_object(Development())
    app.config['CORS_HEADERS'] = 'Content-Type'
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    jwt = JWTManager(app)

    db = MongoEngine(app)

    # ------------------------------------

    # register the blueprint

    app.register_blueprint(api_bp)

    app.register_blueprint(auth_bp)
    # ------This line is only to debug, this print allow see app configuration
    print(app.config)

    return app


app = create_app()

socketio = SocketIO(app)

port = get_port()

host = get_host()

@socketio.on("Return this successfully")
def handle_message(data):
    print("received message: " + data)
