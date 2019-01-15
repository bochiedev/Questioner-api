from datetime import datetime
from .base_models import BaseModels

questions = [
    {
        "id" : 1,
        "createdOn" : datetime.now(),
        "createdBy" : 1,
        "meetup" : 1,
        "title" : "when is the event",
        "body" : "When is this event being held?",
        "upvotes" : 4,
        "downvotes" : 32

    },
    {
        "id" : 2,
        "createdOn" : datetime.now(),
        "createdBy" : 2,
        "meetup" : 2,
        "title" : "where is the event",
        "body" : "Where is this event being held and when is that?",
        "upvotes" : 23,
        "downvotes" : 2,

    },
    {
        "id" : 3,
        "createdOn" : datetime.now(),
        "createdBy" : 3,
        "meetup" : 3,
        "title" : "event about",
        "body" : "What is this event about?",
        "upvotes" : 13,
        "downvotes" : 3,

    }
]

class QuestionModel(BaseModels):

    def __init__(self, user=None, meetup=None, title=None, body=None):
        self.question_id = len(questions) + 1
        self.createdOn = datetime.now()
        self.createdBy = user
        self.meetup = meetup
        self.title = title
        self.body = body
        super().__init__("question")

    def save(self):
        question = {
            "id": self.question_id,
            "createdOn":self.createdOn,
            "createdBy":self.createdBy,
            "meetup":self.meetup,
            "title" : self.title,
            "body" : self.body,
            "upvotes":0,
            "downvotes":0

        }
        save_as = self.save_req(data=question)

        return save_as
