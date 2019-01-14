from flask import jsonify, request, make_response
from app.api.v1.models.auth_models import UserModel
from flask_restful import Resource
from app.api.v1.utils.validators import Validator
import sys


class User(Resource):
    def get(self):
        users = UserModel().return_data()
        return make_response(jsonify({'users': users}), 200)

    def post(self):
        data = request.get_json()
        validate = Validator(data)

        validator = {
            "check_fields": validate.check_fields(),
            "check_password": validate.check_password(),
            "check_email": validate.check_email(),

        }

        for key, value in validator.items():

            if value['message'] == True:
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
                    return make_response(jsonify({'message': resp, "status": 201}), 201)

                else:
                    return make_response(jsonify({"error": "Passwords don't match",
                                                  "status": 400}), 400)
            else:
                return make_response(
                    jsonify({"error": '{}'.format(value['message']), "status": 400}), 400)
