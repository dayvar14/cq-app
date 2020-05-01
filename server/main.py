#!/usr/bin/env python

"""
    main.py:
        Launches the server with the language model specified. It accepts http requests with following json in the body
        { 'question' : 'How are you doing' }
"""

__author__ = "Daniel Ayvar"

from flask import Flask, request
from flask_restful import Resource, Api
import spacy
import sys
import classify as cq

app = Flask(__name__)
api = Api(app)
model_path = ""
en_nlp = ""

def check_arguments():
    if len(sys.argv) < 2:
        print("Enter path for training model...")
        sys.exit(1)

def main():
    print("Starting server...")
    app.run(debug=False)

class Classifier(Resource):

    def post(self):
        json_data = request.get_json()
        q_class = cq.classify(json_data["question"],model_path,en_nlp)

        output_message = {"class":str(q_class[0])}
        return output_message, 201

api.add_resource(Classifier, '/')

if __name__ == '__main__':
    check_arguments()
    model_path = sys.argv[1]
    print("Loading EN_CORE_WEB_MD spacy model...")
    en_nlp = spacy.load("en_core_web_md")
    main()