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

class DownvoteView(Resource):
    def get(self, id):
        question = QuestionModel().return_data(id=id)
        if question is not None:
            question['downvotes'] = question['downvotes'] + 1
            resp = QuestionModel().update(question)
            return make_response(jsonify({'data':resp}),200)
        else:
            return make_response(jsonify({'error':"Data does not exist"}),404)

class UpvoteView(Resource):
    def get(self, id):
        question = QuestionModel().return_data(id=id)
        if question is not None:
            question['upvotes'] = question['upvotes'] + 1
            resp = QuestionModel().update(question)
            return make_response(jsonify({'data':resp}),200)
        else:
            return make_response(jsonify({'error':"Data does not exist"}),404)







# Patch /questions/<question-id>/upvote
# Patch /questions/<question-id>/downvote
