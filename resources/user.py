from flask_restful import Resource
from flask import request
from models.schema.user import UserSchema
from models.user import UserModel

user_schema = UserSchema(many=False)

def get_param():
    data = request.get_json(force=False)
    if data is None:
        data = request.form
    return data

class User(Resource):

    def get(self, name):
        user = UserModel.get_user(name)
        if not user:
            return {
                'message': 'username not exist!'
            }, 403
        return {
            'message': '',
            'user': user_schema.dump(user).data
        }

    def post(self, name):
        # result = user_schema.load(request.json) get_param
        result = user_schema.load(get_param())
        if len(result.errors)> 0:
            return result.errors, 433
        user = UserModel(name,result.data['email'],result.data['password'])    
        user.add_user()
        return {
            'message':'Inser user success',
            'user':user_schema.dump(user)
        }
    def put(self, name):
        result = user_schema.load(request.json)
        if len(result.errors) >0:
            return result.errors, 433
        user = UserModel.get_user(name)
        if not user:
            return{
                'message':'username not exist'
            },403
        user.email= result.data['email'] 
        user.password = result.data['password']
        return {
            'message':'Update user success',
            'user':user_schema.dump(user).data
        }

    def delete(self, name):
        UserModel.delete_user(name)
        return{
            'message': 'Delete done!'
        }

class Users(Resource):
    def get(self):
        return {
            'message': '',
            'users': user_schema.dump(UserModel.get_all_user(),True).data
        }
