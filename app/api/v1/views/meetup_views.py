from flask import Blueprint, jsonify, request, make_response
from flask import Blueprint
from app.api.v1.models.meetup_models import Meetup

meetup = Blueprint('meetup', __name__, url_prefix='/api/v1/meetup/')


@meetup.route('/create', methods=['POST'])
def create_meetup():
    req_data = request.get_json()
    location = req_data['location']
    images = req_data['images']
    topic = req_data['topic']
    happeningOn = req_data['happeningOn']
    tags = req_data['tags']
    createdBy = req_data['createdBy']
    venue = req_data['venue']
    time = req_data['time']


    new_meetup = Meetup(location, happeningOn, tags, images, topic, createdBy, venue ,time)
    meetup = new_meetup.register_meetup()

    return make_response(jsonify(status=201,data=meetup)),201
