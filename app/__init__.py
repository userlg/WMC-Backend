from flask import Flask, Blueprint

from dotenv import load_dotenv, find_dotenv

from .Config.config import Production, Development

from tqdm import tqdm, trange

import colorama as co

import random

import time

import os

###------Simple decoration to the app
def generate_load_bar() -> None:
    co.init()
    green = co.Fore.GREEN
    yellow = co.Fore.YELLOW
    print(green + '\t\t WMC Backend Application \n\n')
    pbar = tqdm(total=50)
    for i in range(5):
        time.sleep(0.2)
        pbar.update(10)
    print(yellow)
    pbar.close()

def get_port() -> int:
    load_dotenv(find_dotenv())
    return os.environ.get('PORT')

def create_app() -> Flask:
    app = Flask(__name__)
    
    #app.config.from_object(Production())
    app.config.from_object(Development())
    
    return app

app = create_app()

port = get_port()