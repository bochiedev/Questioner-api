from flask import jsonify, request, make_response
<<<<<<< HEAD
from app.api.v1.models.meetup_models import MeetupModel
from flask_restplus import Resource
=======
from app.api.v1.models.meetup_models import MeetupModel, MeetupRsvpModel
from flask_restful import Resource
>>>>>>> 6c6d99b26990fe5f8499a11463893adef6d6fa0c

class Meetup(Resource):
    def get(self):
        meetups = MeetupModel().return_data()
        return make_response(jsonify({'meetups':meetups}),200)

    def post(self):
        req_data = request.get_json()
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
        return make_response(jsonify({'data': resp, "status": 201}), 201)

class MeetupRsvp(Resource):
    def get(self,id):
        meetup = MeetupRsvpModel().return_data(id=id)
        return make_response(jsonify({'meetup':meetup}),200)

    def post(self,id):
        req_data = request.get_json()
        meetup = id
        user = req_data['user']


        _b_save = MeetupRsvpModel(meetup,user)
        resp = _b_save.save()
        return make_response(jsonify({'data': resp, "status": 201}), 201)
