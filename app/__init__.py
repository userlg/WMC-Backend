from flask import Flask

from flask_mongoengine import MongoEngine

from .routes.api import api_bp

from .routes.auth import auth_bp

from .config.config import Production, Development

from .libs.modules import get_port

import os


###------Create the main app
def create_app() -> Flask:
    app = Flask(__name__)

    # app.config.from_object(Production())
    app.config.from_object(Development())

    # register the blueprint

    app.register_blueprint(api_bp)

    app.register_blueprint(auth_bp)

    print(app.config)

    return app


app = create_app()

db = MongoEngine(app)



port = get_port()
