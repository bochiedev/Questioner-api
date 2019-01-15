from flask import jsonify, request, make_response
from app.api.v1.models.question_models import QuestionModel
from flask_restful import Resource

class QuestionView(Resource):
    def get(self):
        questions = QuestionModel().return_data()
        return make_response(jsonify({'questions':questions}),200)

    def post(self):
        req_data = request.get_json()

        user = req_data["createdBy"]
        meetup = req_data["meetup"]
        title = req_data["title"]
        body = req_data["body"]
        _b_save = QuestionModel(user, meetup, title, body)
        resp = _b_save.save()
        return make_response(jsonify({'data': resp, "status": 201}), 201)


# Patch /questions/<question-id>/upvote
# Patch /questions/<question-id>/downvote
