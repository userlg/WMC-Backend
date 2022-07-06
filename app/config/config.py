from dotenv import load_dotenv, find_dotenv

import os

import uuid

load_dotenv(find_dotenv())

class Config(object):
    TESTING = False
    SECRET_KEY = str(uuid.uuid4())
    UPLOAD_FOLDER = os.getcwd() + '\\uploads'
    

class Production(Config):
    ENV = os.environ.get('ENV_PRODUCTION')
    MONGODB_SETTINGS= { "db": "WMC_ENTERPRISE_PROD"}
    DEBUG = False

class Development(Config):
     ENV = os.environ.get('ENV_DEVELOPMENT')
     MONGODB_SETTINGS = { 
     "db": os.environ.get("DB_DEV"),
    # "port": os.environ.get("DB_PORT"),
    # "host": os.environ.get("HOST_DEV")
     }
     DEBUG = True

class Test(Config):
    TESTING = True


'''
app.config['MONGODB_SETTINGS'] = {
    'db': 'project1',
    'username':'webapp',
    'password':'pwd123'
}

app.config['MONGODB_SETTINGS'] = {
    'db': 'project1',
    'host': 'mongodb://localhost/database_name'
}

'''