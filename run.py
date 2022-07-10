from app import socketio, app as application, port, host

from app.libs.modules import generate_load_bar

if __name__ == '__main__':
    generate_load_bar()
    socketio.run(application, host=host, port=port) 
    #application.run(host='0.0.0.0', port=port)
   

################################################   
# This project was created by USERLG
################################################