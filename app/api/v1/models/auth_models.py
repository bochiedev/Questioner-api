from flask import abort, jsonify
from datetime import datetime

Users = []

class User(object):

    def __init__(self, firstname, lastname, othername, phoneNumber, username, email, password):
        self.user_id = len(Users) + 1
        self.email = email
        self.firstname = firstname
        self.lastname = lastname
        self.othername = othername
        self.phoneNumber = phoneNumber
        self.username = username
        self.registered = datetime.now()
        self.password = password

    def register_user(self):
        user = {
            "id": self.user_id,
            'firstname': self.firstname,
            'lastname': self.lastname,
            'othername': self.othername,
            "username": self.username,
            "email": self.email,
            'phoneNumber': self.phoneNumber,
            'registered': self.registered,
            "password": self.password,
            'isAdmin': False,
        }

        return user
