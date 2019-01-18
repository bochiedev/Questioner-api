from flask import jsonify, request, make_response
from app.api.v1.models.comment_models import CommentModel
from flask_restful import Resource

class CommentView(Resource):
    def get(self):
        comments = CommentModel().return_data()
        return make_response(jsonify({'comments':comments}),200)

    def post(self):
        req_data = request.get_json()

        user = req_data["createdBy"]
        question = req_data["question"]
        title = req_data["title"]
        body = req_data["body"]
        _b_save = CommentModel(user, question, title, body)
        resp = _b_save.save()
        return make_response(jsonify({'data': resp, "status": 201}), 201)
