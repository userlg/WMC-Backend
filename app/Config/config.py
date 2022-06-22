from dotenv import load_dotenv, find_dotenv

import os

import uuid

load_dotenv(find_dotenv())

class Config(object):
    TESTING = False
    SECRET_KEY = str(uuid.uuid4())

class Production(Config):
    ENV = os.environ.get('ENV_PRODUCTION')
    DEBUG = False

class Development(Config):
     ENV = os.environ.get('ENV_DEVELOPMENT')
     DEBUG = True

class Test(Config):
    TESTING = True