from flask import Response, make_response

from datetime import datetime as dt


#------With this function we can generate the apropiate response depending of the status

def generate_response(message : str, code : int) -> Response:
    response = make_response({"message" : message, "date": dt.now()})
    response.status_code = code
    return response

def generate_response_jwt(message : str, jwt : str, code : int) -> Response:
    response = make_response({"message" : message, "access_token": jwt, "date": dt.now()})
    response.status_code = code
    return response