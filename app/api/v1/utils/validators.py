import sys
import re


class Validator():

    def __init__(self, data):
        self.data = data
        self.email = data['email']
        self.password = data['password']

    def check_fields(self):
        for key, value in self.data.items():
            if not value:
                resp = {
                    "message": '{} field Cannot be empty'.format(key)
                }
                return resp
            else:
                resp = {
                    "message": True
                }
                return resp

    def check_email(self):
        if not re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", self.email):
            resp = {
                "message": 'Please enter a valid email'
            }
            return resp
        else:
            resp = {
                "message": True
            }
            return resp

    def check_password(self):
        password = self.password

        if len(password) < 6:
            resp = {
                "message": 'password field must be more than 6 characters'
            }
            return resp

        elif not re.search("[a-z]", password):
            resp = {
                "message": 'password field must contain atleast 1 lowercase letter'
            }
            return resp

        elif not re.search("[A-Z]", password):
            resp = {
                "message": 'password field must contain atleast 1 uppercase letter'
            }
            return resp

        elif not re.search("[0-9]", password):
            resp = {
                "message": 'password field must contain atleast 1 digit'
            }
            return resp

        elif not re.search("[_@$#!*]", password):
            resp = {
                "message": 'password field must contain one of the following characters _ @ $ # ! *'
            }
            return resp
        else:
            resp = {
                "message": True
            }
            return resp
