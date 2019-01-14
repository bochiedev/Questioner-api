from datetime import datetime
from .base_models import BaseModels

Users = [
    {
        "id": 1,
        'firstname': "firstname",
        'lastname': "lastname",
        'othername': "othername",
        "username": "username",
        "email": "email@gmail.com",
        'phoneNumber': "254722241161",
        'registered': "registered",
        "password": "password",
        'isAdmin': True,
    },
    {
        "id": 2,
        'firstname': "firstname2",
        'lastname': "lastname2",
        'othername': "othername2",
        "username": "username2",
        "email": "email2@gmail.com",
        'phoneNumber': "254722241162",
        'registered': datetime.now(),
        "password": "password2",
        'isAdmin': False,
    },
    {
        "id": 3,
        'firstname': "firstname3",
        'lastname': "lastname3",
        'othername': "othername3",
        "username": "username3",
        "email": "email3@gmail.com",
        'phoneNumber': "254722241163",
        'registered': datetime.now(),
        "password": "password3",
        'isAdmin': False,
    }
]


class UserModel(BaseModels):

    def __init__(self, firstname=None, lastname=None, othername=None, phoneNumber=None, username=None, email=None, password=None):
        self.user_id = len(Users) + 1
        self.email = email
        self.firstname = firstname
        self.lastname = lastname
        self.othername = othername
        self.phoneNumber = phoneNumber
        self.username = username
        self.registered = datetime.now()
        self.password = password
        super().__init__("user")



    def save(self):

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
        save_as = self.save_req(data=user)
        return save_as
