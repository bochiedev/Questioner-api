from flask import jsonify, request, make_response
from flask_restful import Resource

class Home(Resource):
    def get(self):
        return make_response(jsonify({'data':[],'status':200}),200)
