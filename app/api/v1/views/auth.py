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
        check_fields = validate.check_fields()
        check_password = validate.check_password()
        check_email = validate.check_email()
        check_password_match = validate.pass_match()

        if check_fields != True:
            return make_response(
                jsonify({"error": check_fields, "status": 400}), 400)

        elif check_email != True:
            return make_response(
                jsonify({"error": check_email, "status": 400}), 400)
        elif check_password != True:
            return make_response(
                jsonify({"error": check_password, "status": 400}), 400)
        elif check_password_match != True:
            return make_response(
                jsonify({"error": check_password_match, "status": 400}), 400)

        else:

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

            _b_save = UserModel(firstname, lastname, othername,
                                phoneNumber, username, email, password)

            resp = _b_save.save()
            return make_response(jsonify({'message': resp, "status": 201}), 201)


class UserLogin(Resource):
    def post(self):
        data = request.get_json()
        email = data['email']
        password = data['password']

        validate = Validator(data)

        check_fields = validate.check_fields()
        check_email = validate.check_email()

        if check_fields != True:
            resp = {
                "error" : check_fields,
                "status_code" : 400
            }

        elif check_email != True:
            resp = {
                "error" : check_email,
                "status_code" : 400
            }
        else:
            try:
                user = UserModel().return_data(email=email)
                print(user, file=sys.stdout)
                data_list = []

                if user['password'] == password:
                    resp = {
                        "message" : "Successfully Logged In",
                        "status_code" : 200

                    }

                    return make_response(jsonify({"message": "Successfully Logged In",
                                                  "status": 200}), 200)
                else:
                    resp = {
                        "error" : "wrong email or Password",
                        "status_code" : 401

                    }

            except:
                resp = {
                    "error" : "User does not exist",
                    "status_code" : 404

                }

        return make_response(jsonify({"data": resp,
                                      "status": resp['status_code']}), resp['status_code'])
