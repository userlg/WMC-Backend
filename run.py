from app import app, port

import colorama as co

if __name__ == '__main__':
    co.init()

    green = co.Fore.YELLOW

    app.run(host='0.0.0.0', port=port)


################################################   
# This project was created by USERLG
################################################