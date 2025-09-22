# 代码生成时间: 2025-09-22 14:11:59
import numpy as np
from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    api = Api(app)
    CORS(app)
    
    # Index Resource
    class Index(Resource):
        def get(self):
            """
            Index API endpoint that returns a simple message.
            """
            return {'message': 'Welcome to the RESTful API'}
    
    # Numpy Resource
    class NumpyOperations(Resource):
        def post(self):
            """
            Numpy Operations API endpoint that performs operations on numpy arrays.
            "