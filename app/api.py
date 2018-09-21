"""Import flask"""
import sys
from flask import Flask, jsonify, request, make_response
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Home(Resource):
    def get(self):
        return jsonify({'message': 'Welcome to Stackoverflow-lite'})

api.add_resource(Home, '/api/v1')

if __name__ == '__main__':
    app.run(debug=True)