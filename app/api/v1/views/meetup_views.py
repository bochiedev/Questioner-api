from flask import jsonify, request, make_response
from app.api.v1.models.meetup_models import MeetupModel,MeetupRsvpModel
from app.api.v1.models.auth_models import UserModel

from flask_restplus import Resource

class Meetup(Resource):
    def get(self):
        meetups = MeetupModel().return_data()
        return make_response(jsonify({'meetups':meetups}),200)

    def post(self):
        req_data = request.get_json()
        data_list = []
        location = req_data['location']
        images = req_data['images']
        topic = req_data['topic']
        happeningOn = req_data['happeningOn']
        tags = req_data['tags']
        createdBy = req_data['createdBy']
        venue = req_data['venue']
        time = req_data['time']


        _b_save = MeetupModel(location, happeningOn, tags, images, topic, createdBy, venue ,time)
        resp = _b_save.save()


        data_list.append(resp)

        return make_response(jsonify({'data': data_list, "status": 201}), 201)

class MeetupRsvp(Resource):
    def get(self,id):
        meetup = MeetupRsvpModel().return_data(id=id)
        return make_response(jsonify({'meetup':meetup}),200)

    def post(self,id):
        req_data = request.get_json()
        meetup_id = id
        user = req_data['user']
        data_list = []

        try:
            meetup = MeetupModel().return_data(id=meetup_id)

            if meetup:
                _b_save = MeetupRsvpModel(meetup_id,user)
                resp = _b_save.save()



            data_list.append(resp)
            return make_response(jsonify({'data': data_list, "status": 201}), 201)
        except:
            resp = {
                "error": "Meetup does not exist",
                "status_code": 404
            }
            return make_response(jsonify({'error': resp['error'], "status_code ": resp['status_code']}), resp['status_code'])



    def delete(self,id):
        req_data = request.get_json()
        meetup = id
        user = req_data['user']

        try:

            user = UserModel().return_data(id=user)
            meetup = MeetupModel().return_data(id=meetup)
            if meetup['createdBy'] != user['id']:
                return make_response(jsonify({'error': "Unauthorized", "status": 401}), 401)

            else:
                _b_save = MeetupModel()
                resp = _b_save.delete(id=meetup['id'])
                return make_response(jsonify({'message': "Meetup deleted Successfully", "status": 200}), 200)

        except:
            return make_response(jsonify({'error': "Object does not exist", "status": 404}), 404)
