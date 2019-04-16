from flask import Flask
from flask_restful import Api
from flask_restful import Resource


class PrintHelloWorld(Resource):
    def get(self):
        return{
            'message':'Hello World'
        },200

app = Flask(__name__)
api =Api(app)

api.add_resource(PrintHelloWorld,'/print_hello_world')

if __name__ == "__main__":
    app.run()