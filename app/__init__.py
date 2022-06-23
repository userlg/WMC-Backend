from flask import Flask, Blueprint

from flask_mongoengine import MongoEngine

from .routes.api import api_bp

from .routes.auth import auth_bp

from .Config.config import Production, Development

from .libs.modules import get_port

import os




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

#print(app.config['MONGODB_SETTINGS'])

port = get_port()