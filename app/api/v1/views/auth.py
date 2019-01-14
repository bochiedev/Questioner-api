from flask import jsonify, request, make_response
from app.api.v1.models.auth_models import UserModel
from flask_restful import Resource
from app.api.v1.utils.validators import Validator
import sys


class User(Resource):
    def get(self):
        users = UserModel().return_data()
        return make_response(jsonify({'users': users}), 200)

    # def post(self):
    #     data = request.get_json()
    #     validate = Validator(data)
    #
    #     check_fields = validate.check_fields()
    #     check_password = validate.check_password()
    #     check_email = validate.check_email()
    #
    #     if check_fields != True:
    #         return make_response(
    #             jsonify({"error": check_fields['message'], "status": 400}), 400)
    #
    #     elif check_email != True:
    #         return make_response(
    #             jsonify({"error": check_email['message'], "status": 400}), 400)
    #
    #     elif check_password != True:
    #         return make_response(
    #             jsonify({"error": check_password['message'], "status": 400}), 400)
    #
    #     else:
    #         firstname = data['firstname']
    #         lastname = data['lastname']
    #         othername = data['othername']
    #         email = data['email']
    #         phoneNumber = data['phoneNumber']
    #         username = data['username']
    #         registered = data['registered']
    #         isAdmin = data['isAdmin']
    #         password = data['password']
    #         confirm_password = data['confirm_password']
    #
    #         if password == confirm_password:
    #             _b_save = UserModel(firstname, lastname, othername,
    #                                 phoneNumber, username, email, password)
    #
    #             resp = _b_save.save()
    #             return make_response(jsonify({'message': resp, "status": 201}), 201)
    #
    #         else:
    #             return make_response(jsonify({"error": "Passwords don't match",
    #                                           "status": 400}), 400)

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
