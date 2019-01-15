from flask import jsonify, request, make_response
from app.api.v1.models.meetup_models import MeetupModel
from flask_restful import Resource

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


# GET meetup  id

# GET upcoming meetups
# POST /meetups/<meetup-id>/rsvps
