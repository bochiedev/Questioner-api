import unittest
from flask import json
from datetime import datetime
from app import create_app
import json

class TestQuestioner(unittest.TestCase):
    """This class represents storemanger products posted test class"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app("testing")
        self.client = self.app.test_client()
        self.user_data = {
                            'firstname' : "james",
                            'lastname' : "Kabochi",
                            'othername' : "Gakuru",
                            'email' : "bochirgfx@gmail.com",
                            'phoneNumber' : "254722241161",
                            'username' : "bochie",
                            'registered' : "12-2-2019",
                            'isAdmin' : False,
                            'password':"password",
                            'confirm_password':"password"

                            }
        self.wrong_user_data = {
                            'firstname' : "james",
                            'lastname' : "Kabochi",
                            'othername' : "Gakuru",
                            'email' : "bochirgfx@gmail.com",
                            'phoneNumber' : "254722241161",
                            'username' : "bochie",
                            'registered' : "12-2-2019",
                            'isAdmin' : False,
                            'password':"password",
                            'confirm_password':"confirm_password"
                            }


    def test_register_user(self):
        """Testing posting a meetup."""

        response = self.client.post(
            '/api/v1/auth/register', data=json.dumps(self.user_data), content_type='application/json')

        res = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 201)
    def test_wrong_password_registeration(self):
        """Testing posting a meetup."""

        response = self.client.post(
            '/api/v1/auth/register', data=json.dumps(self.wrong_user_data), content_type='application/json')

        res = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 400)



if __name__=='__main__':
    unittest.main()
