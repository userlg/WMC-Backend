from flask import Flask, Blueprint

from dotenv import load_dotenv, find_dotenv

from flask_mongoengine import MongoEngine

from .routes.api import api_bp

from .routes.auth import auth_bp

from .Config.config import Production, Development

import os


###-------Load the port 
def get_port() -> int:
    load_dotenv(find_dotenv())
    return os.environ.get('PORT')

###------Create the main app
def create_app() -> Flask:
    app = Flask(__name__)
    
    #app.config.from_object(Production())
    app.config.from_object(Development())

    #register the blueprint

    app.register_blueprint(api_bp)

    app.register_blueprint(auth_bp)
    
    return app

app = create_app()

db = MongoEngine(app)

print(app.config['MONGODB_SETTINGS'])

port = get_port()