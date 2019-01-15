from flask import jsonify, request, make_response
from app.api.v1.models.auth_models import UserModel
from flask_restful import Resource
from app.api.v1.utils.validators import Validator
from app.api.v1.utils.auth import login
import sys


class User(Resource):
    def get(self):
        users = UserModel().return_data()
        return make_response(jsonify({'users': users}), 200)

    def post(self):
        data = request.get_json()
        validate = Validator(data)
        firstname = data['firstname']
        lastname = data['lastname']
        othername = data['othername']
        email = data['email']
        phoneNumber = data['phoneNumber']
        username = data['username']
        registered = data['registered']
        isAdmin = data['isAdmin']
        password = data['password']
        confirm_password = data['confirm_password']

        if password == confirm_password:
            _b_save = UserModel(firstname, lastname, othername,
                                phoneNumber, username, email, password)

            resp = _b_save.save()
            data_list = []
            data_list.append(resp)
            return make_response(jsonify({'data': data_list, "status": 201}), 201)

        else:
            return make_response(jsonify({"error": "Passwords don't match",
                                          "status": 400}), 400)

class UserLogin(Resource):
    def post(self):
        data = request.get_json()
        email = data['email']
        password = data['password']

        user = UserModel().return_data(email=email)
        print(user, file=sys.stdout)
        data_list = []

        if user != None:
            if user['password'] == password:

                return make_response(jsonify({"message": "Successfully Logged In",
                                              "status": 200}), 200)
            else:
                return make_response(jsonify({"error": "wrong password",
                                              "status": 401}), 401)
