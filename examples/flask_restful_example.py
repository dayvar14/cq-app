from flask import Flask, request 
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return { 'about' : 'Hello World!'}

    def post(self):
        client_json = request.get_json()
        return {'Request' : client_json}, 201

class Multi(Resource):
    def get(self, num):
        return { 'result' : num*num}

api.add_resource(HelloWorld, '/')
api.add_resource(Multi, '/multi/<int:num>')

if __name__ == '__main__':
    app.run(debug=True)