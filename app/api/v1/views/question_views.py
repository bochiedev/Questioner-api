from flask import jsonify, request, make_response
from app.api.v1.models.question_models import QuestionModel
from app.api.v1.models.meetup_models import MeetupModel
from app.api.v1.models.auth_models import UserModel
from flask_restplus import Resource


class QuestionView(Resource):
    def get(self):
        questions = QuestionModel().return_data()
        return make_response(jsonify({'questions': questions}), 200)

    def post(self):
        req_data = request.get_json()

        user_id = req_data["createdBy"]
        meetup_id = req_data["meetup"]
        title = req_data["title"]
        body = req_data["body"]
        data_list = []

        try:
            user = UserModel().return_data(id=user_id)
            meetup = MeetupModel().return_data(id=meetup_id)

            _b_save = QuestionModel(user_id, meetup_id, title, body)
            resp = _b_save.save()
            data_list.append(resp)
            return make_response(jsonify({'data': data_list, "status": 201}), 201)

        except:

            return make_response(jsonify({'error': "object not Found", "status": 404}), 404)


class DownvoteView(Resource):
    def get(self, id):
        data_list = []
        try:
            question = QuestionModel().return_data(id=id)
            question['downvotes'] = question['downvotes'] + 1
            resp = QuestionModel().update(question)
            data_list.append(resp)
            return make_response(jsonify({'data': data_list, "status": 200}), 200)

        except:
            return make_response(jsonify({'error': "Question not Found", "status": 404}), 404)

class UpvoteView(Resource):
    def get(self, id):
        data_list = []
        try:
            question = QuestionModel().return_data(id=id)
            question['upvotes'] = question['upvotes'] + 1
            resp = QuestionModel().update(question)
            data_list.append(resp)
            return make_response(jsonify({'data': data_list, "status": 200}), 200)
         except:
              return make_response(jsonify({'error': "Question not Found", "status": 404}), 404)

