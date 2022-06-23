'''
This file contains all methods and logic to managment the requests and the operations

'''

from tqdm import tqdm

import colorama as co

import time



###------Simple decoration to the app
def generate_load_bar() -> None:
    co.init()
    green = co.Fore.GREEN
    yellow = co.Fore.YELLOW
    print(green + '\n\n\t\t <------WMC BACKEND APPLICATION------> \n\n')
    pbar = tqdm(total=50)
    for i in range(5):
        time.sleep(0.2)
        pbar.update(10)
    print(yellow)
    pbar.close()
