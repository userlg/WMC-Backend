from app import app as application, port

from app.libs.modules import generate_load_bar

import asyncio

if __name__ == '__main__':
    
    generate_load_bar()
    
    application.run(host='0.0.0.0', port=port)


################################################   
# This project was created by USERLG
################################################