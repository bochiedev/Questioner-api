from flask import Blueprint, jsonify, request, make_response
from flask import Blueprint
from app.api.v1.models.auth_models import User

auth = Blueprint('auth', __name__, url_prefix='/api/v1/auth/')


@auth.route('/register', methods=['POST'])
def register():
    data = request.get_json()
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
        new_user = User(firstname, lastname, othername,
                        phoneNumber, username, email, password)
        user = new_user.register_user()

        return make_response(jsonify(user,
                                     {"message": "User created successfull!"})), 201
    else:
        return make_response(
            jsonify({"message": "Passwords don't match"})), 409
