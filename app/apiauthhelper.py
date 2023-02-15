from .models import User
from flask import request
import base64

def basic_auth_required(func):
    def decorated(*args, **kwargs):
        
        if 'Authorization' in request.headers:
            val = request.headers['Authorization']
            encoded_version = val.split()[1]
            x = base64.b64decode(encoded_version.encode("ascii")).decode('ascii')
            
            username, password = x.split(':')
        else:
            return {
                'status': 'not ok',
                'message': 'Please add an Authorzation Header with the Basic Auth Format.'
            }
            
        user = User.query.filter_by(username=username).first()
        if user:
            if user.password == password:
                #give token
                return func(user=user, *args, **kwargs)
            else:
                return {
                    'status': 'not ok',
                    'message': 'password is incorrect'
                }
    return decorated

def token_auth_required(func):
    def decorated(*args, **kwargs):
        if 'Authorization' in request.headers:
            val = request.headers['Authorization']
            
            _, token = val.split()
        else:
            return {
                'status': 'not ok',
                'message': 'Please add Authorization header with token auth format'
            }
            
        user = User.query.filter_by(apitoken=token).first()
        if user:
                #give token
                return func(user=user, *args, **kwargs)
        else:
            return {
                'status': 'not ok',
                'message': 'not valid user'
            }
    return decorated