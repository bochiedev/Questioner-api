from datetime import datetime
from .base_models import BaseModels

meetups = [
    {
        "id":1,
        "location": "Kisumu",
        "venue": "Senteu",
        "images": [],
        "topic": "Flutter",
        "happeningOn": "12-2-2017",
        "time": "1000",
        "tags": ["programming", "flutter"],
        "createdBy": 2,
    },
    {
        "id":2,
        "location": "Nairobi",
        "venue": "Ihub",
        "images": [],
        "topic": "Dev Fest",
        "happeningOn": "12-2-2019",
        "time": "1800",
        "tags": ["programming", "Js"],
        "createdBy": 1,
    }
]

meetup_rsvp = [
    {
	"id" : 1,
	"meetup" : 2,
	"createdBy" : 2,
    'bookedOn': datetime.now(),
    },
    {
	"id" : 2,
	"meetup" : 2,
	"createdBy" : 1,
    'bookedOn': datetime.now(),
    }
]

class MeetupModel(BaseModels):

    def __init__(self, location=None, happeningOn=None, tags=None, images=None, topic=None, createdBy=None, venue=None,time=None):
        self.meetup_id = len(meetups) + 1
        self.createdOn = datetime.now()
        self.createdBy = createdBy
        self.location = location
        self.images = images
        self.topic = topic
        self.happeningOn = happeningOn
        self.tags = tags
        self.venue = venue
        self.time = time

        super().__init__("meetup")

    def save(self):
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
            "time":self.time
        }
        save_as = self.save_req(data=meetup)

        return save_as

class MeetupRsvpModel(BaseModels):

    def __init__(self, meetup=None, user=None ):
        self.meetup_rsvp_id = len(meetup_rsvp) + 1
        self.bookedOn = datetime.now()
        self.createdBy = user
        self.meetup = meetup

        super().__init__("meetuprsvp")

    def save(self):
        _rsvp = {
            "id": self.meetup_rsvp_id,
            "bookedOn" : self.bookedOn,
            "createdBy":self.createdBy,
            "meetup" : self.meetup
        }
        save_as = self.save_req(data=_rsvp)

        return save_as
