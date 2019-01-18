from datetime import datetime
import sys

user_list = [
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

meetup_list = [
    {
        "id":1,
        "location": "Kisumu",
        "venue": "Senteu",
        "images": [],
        "topic": "Flutter",
        "happeningOn": "12-2-2017",
        "time": "1000",
        "tags": ["programming", "flutter"],
        "createdBy": 2,
    },
    {
        "id":2,
        "location": "Nairobi",
        "venue": "Ihub",
        "images": [],
        "topic": "Dev Fest",
        "happeningOn": "12-2-2019",
        "time": "1800",
        "tags": ["programming", "Js"],
        "createdBy": 1,
    }
]

question_list = [
    {
        "id": 1,
        "createdOn": datetime.now(),
        "createdBy": 1,
        "meetup": 1,
        "title": "when is the event",
        "body": "When is this event being held?",
        "upvotes": 4,
        "downvotes": 32

    },
    {
        "id": 2,
        "createdOn": datetime.now(),
        "createdBy": 2,
        "meetup": 2,
        "title": "where is the event",
        "body": "Where is this event being held and when is that?",
        "upvotes": 23,
        "downvotes": 2,

    },
    {
        "id": 3,
        "createdOn": datetime.now(),
        "createdBy": 3,
        "meetup": 3,
        "title": "event about",
        "body": "What is this event about?",
        "upvotes": 13,
        "downvotes": 3,

    }
]

comment_list = [
    {
        "id" : 1,
        "createdOn" : datetime.now(),
        "createdBy" : 1,
        "question" : 1,
        "title" : "Great question",
        "body" : "I also wanted to know this",

    },
    {
        "id" : 2,
        "createdOn" : datetime.now(),
        "createdBy" : 2,
        "question" : 2,
        "title" : "good question",
        "body" : "and also what is the time",

    },
    {
        "id" : 3,
        "createdOn" : datetime.now(),
        "createdBy" : 3,
        "question" : 3,
        "title" : "Dont ask this",
        "body" : "Why are you asking such question",

    }
]


class BaseModels:

    def __init__(self, db):
        self.db = db
        self.user_db = user_list
        self.meetup_db = meetup_list
        self.question_db = question_list
        self.comment_db = comment_list


    def check_db(self):
        if self.db == "user":
            db = self.user_db
            return db

        elif self.db == "meetup":
            db = self.meetup_db
            return db

        elif self.db == "question":
            db = self.question_db
            return db
        elif self.db == "comment":
            db = self.comment_db
            return db

    def return_data(self, email=None, id=None,username=None):
        data = self.check_db()
        _data = None
        if email is not None:
            for item in data:
                if item['email'] == email:
                    _data = item
            return _data

        elif id is not None:
            for item in data:
                if item['id'] == id:
                    _data = item

            return _data
        elif username is not None:
            for item in data:
                if item['username'] == id:
                    _data = item

            return _data
        return data

    def save_req(self, data={}):
        db = self.check_db()
        if not data:
            return "no data to save"


        return data

    def delete(self, id):
        db = self.check_db()
        i = 0
        for item in db:
            i += 1
            if item['id'] == id:
                del db[i]
                message = "Deleted Successfully"
                break

        return message
      
     def update(self, data={}):
        db = self.check_db()
        if not data:
            return "no data "
        else:
            return data

