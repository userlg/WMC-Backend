from flask import Flask, Blueprint

from dotenv import load_dotenv, find_dotenv

from .Config.config import Production, Development

import os

def get_port() -> int:
    load_dotenv(find_dotenv())
    return os.environ.get('PORT')

def create_app() -> Flask:
    app = Flask(__name__)
    
    app.config.from_object(Production())
    #app.config.from_object(Development())

    print(app.config)
    
    return app

app = create_app()

port = get_port()