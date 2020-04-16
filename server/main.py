from flask import Flask, request 
from flask_restful import Resource, Api
from cq import classify
import json

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def post(self):
        json_data = request.get_json()
        output_message = classify(json_data["message"])
        return {"message": output_message}, 201

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)