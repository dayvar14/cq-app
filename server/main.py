#!/usr/bin/env python

"""
    server.py:

"""

__author__ = "Daniel Ayvar"

from flask import Flask, request
from flask_restful import Resource, Api
import spacy
import classify as cq

app = Flask(__name__)
api = Api(app)

class Classifier(Resource):
    def post(self):
        json_data = request.get_json()
        q_class = cq.classify(json_data["question"],"server/train_5500.model",en_nlp)

        output_message = {"class":str(q_class[0])}
        return output_message, 201

api.add_resource(Classifier, '/')

if __name__ == '__main__':
    print("Loading EN_CORE_WEB_MD spacy model...")
    en_nlp = spacy.load("en_core_web_md")
    print("Starting server...")
    app.run(debug=False)