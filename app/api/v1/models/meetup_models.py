from flask import abort, jsonify
from datetime import datetime

Meetups = []

class Meetup(object):

    def __init__(self, location, happeningOn, tags, images, topic, createdBy, venue ,time):
        self.meetup_id = len(Meetups) + 1
        self.createdOn = datetime.now(),
        self.createdBy = createdBy,
        self.location = location ,
        self.images = images,
        self.topic = topic ,
        self.happeningOn = happeningOn ,
        self.tags = tags ,
        self.venue = venue ,
        self.time = time ,



    def register_meetup(self):
        meetup = {
            "id": self.meetup_id,
            "createdOn" : self.createdOn,
            "location" : self.location,
            "images" : self.images,
            "topic" : self.topic,
            "happeningOn" : self.happeningOn,
            "tags" : self.tags,
            "createdBy":self.createdBy,
            "venue":self.venue,
            "time":self.time,

        }


        return meetup
