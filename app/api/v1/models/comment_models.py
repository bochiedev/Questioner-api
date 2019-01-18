from datetime import datetime
from .base_models import BaseModels

comments = [
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

class CommentModel(BaseModels):

    def __init__(self, user=None, question=None, title=None, body=None):
        self.question_id = len(comments) + 1
        self.createdOn = datetime.now()
        self.createdBy = user
        self.question = question
        self.title = title
        self.body = body
        super().__init__("comment")

    def save(self):
        comment = {
            "id": self.question_id,
            "createdOn":self.createdOn,
            "createdBy":self.createdBy,
            "question":self.question,
            "title" : self.title,
            "body" : self.body,

        }
        save_as = self.save_req(data=comment)

        return save_as
