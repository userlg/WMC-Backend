from dotenv import load_dotenv, find_dotenv

import os

load_dotenv(find_dotenv())

class Config(object):
    TESTING = False
    SECRET_KEY = os.environ.get("SECRET_KEY")

class Production(Config):
    ENV = os.environ.get('ENV_PRODUCTION')
    DEBUG = False

class Development(Config):
     ENV = os.environ.get('ENV_DEVELOPMENT')
     DEBUG = True

class Test(Config):
    TESTING = True