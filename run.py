from app import app, port, generate_load_bar

if __name__ == '__main__':
    
    generate_load_bar()
    
    app.run(host='0.0.0.0', port=port) 


################################################   
# This project was created by USERLG
################################################