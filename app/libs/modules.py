'''
This file contains all methods and logic to managment the requests and the operations

'''

from tqdm import tqdm

from dotenv import load_dotenv, find_dotenv

import colorama as co

import time

import os


###-------Load the port 
def get_port() -> int:
    load_dotenv(find_dotenv())
    return os.environ.get('PORT')



###------Simple decoration to the app
def generate_load_bar() -> None:
    co.init()
    green = co.Fore.GREEN
    yellow = co.Fore.YELLOW
    blue = co.Fore.BLUE

    print(green + '\n\n\t\t <------WMC BACKEND APPLICATION------------> \n\n')
    print(yellow + '\t\t <------SERVER RUNNING ON PORT: '+ blue + get_port() + yellow +' ------> \n\n' + green)
    pbar = tqdm(total=50)
    for i in range(5):
        time.sleep(0.2)
        pbar.update(10)
    print(yellow)
    pbar.close()
