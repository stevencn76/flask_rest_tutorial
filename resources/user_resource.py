import jwt
from flask import request
from flask_restful import Resource

from common.constants import LOGIN_SECRET
from resources import api
from services.user_service import UserService


class LoginResource(Resource):
    def post(self):
        try:
            request_json = request.json
            if request_json:
                username = request_json.get('username', None)
                password = request_json.get('password', None)

                user_model = UserService().login(username, password)
                if user_model:
                    user_json = user_model.serialize()
                    jwt_token = jwt.encode(user_json, LOGIN_SECRET, algorithm='HS256')
                    user_json['token'] = jwt_token

                    return user_json
                else:
                    return {'error': 'Username or password error'}, 401
            else:
                return {'error': 'Please provide username and password info as a json'}, 400
        except Exception as error:
            return {'error': f'{error}'}, 400


api.add_resource(LoginResource, '/login')
