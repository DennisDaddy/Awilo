"""Import flask"""
import sys
from flask import Flask, jsonify, request, make_response
from flask_restful import Resource, Api

from app.models import *
app = Flask(__name__)
api = Api(app)

class Home(Resource):
    """"This is a class for root endpoint"""

    def get(self):
        """"This is a method for getting root endpoint using get request"""
        return jsonify({'message': 'Welcome to Stackoverflow-lite'})

class QuestionList(Resource):
    """This is a class for questions without IDs"""
    
    def get(self):
        """This is a method for getting a list of questions using GET request"""
        my_list = []
        try:
            cur.execute("SELECT * FROM questions")
            rows = cur.fetchall()
            for row in rows:
                id = row[0]
                title = row[1]
                content = row[2]
                my_list.append({"id":id, "title":title, "content":content})
        except:
            return jsonify({"message": "cannot retrieve questions"})
        return jsonify({"rows": my_list})
        

api.add_resource(Home, '/api/v1')
api.add_resource(QuestionList, '/api/v1/questions', endpoint='questions')
# api.add_resource(Question, '/api/v1/questions/<int:id>', endpoint='question')
if __name__ == '__main__':
    app.run(debug=True)
