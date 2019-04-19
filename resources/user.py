from flask_restful import Resource
from flask import request
from models.schema.user import UserSchema
users = []
user_schema= UserSchema()


class User(Resource):

    def get(self, name):
        find = [item for item in users if item['name'] == name]
        if len(find) == 0:
            return {
                'message': 'username not exist!'
            }, 403
        user = find[0]
        if not user:
            return {
                'message': 'username not exist!'
            }, 403
        return {
            'message': '',
            'user': user
        }

    def post(self, name):
        result = user_schema.load(request.json)
        if len(result.errors)> 0:
            return result.errors, 433
        user = {
            'name': name,
            'email': result.data['email'],
            'password': result.data['password']
        }
        global users
        users.append(user)
        return {
            'message':'Inser user success',
            'user':user
        }
    def put(self, name):
        result = user_schema.load(request.json)
        if len(result.errors) >0:
            return result.errors, 433

        find = [item for item in users if item['name']==name]
        if len(find) == 0:
            return{
                'message':'username not exist'
            },403
        user = find[0]   
        user['email']= result.data['email'] 
        user['password'] = result.data['password']
        return {
            'message':'Update user success',
            'user':user
        }

    def delete(self, name):
        global users
        users = [item for item in users if item['name'] != name]
        return{
            'message': 'Delete done!'
        }


class Users(Resource):
    def get(self):
        return {
            'message': '',
            'users': users
        }
