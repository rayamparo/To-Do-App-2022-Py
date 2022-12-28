from src.app import app
from json import dumps
from flask import request, Response
import src.services.user_services as services
from src.models.user_model import UserEncoder

#Create new user
@app.route('/user/create', methods=['POST'])
def create_user():
    req_body = request.get_json()
    email = req_body['email']
    password = req_body['password']
    name = req_body['name']
    created_user = services.create_user(email, password, name)
    if(created_user == 'Email has already been registered'):
        return Response('Email has already been registered.', status=200)
    return Response('User succesfully created', status=200)


#Login user
@app.route('/user/login', methods=['POST'])
def user_login():
    req_body = request.get_json()
    email = req_body['email']
    password = req_body['password']
    login = services.user_login(email, password)
    if(login == 'Password incorrect' or login == 'No user is associated with this email'):
        return Response(login, status=200)
    return dumps(login, cls=UserEncoder)