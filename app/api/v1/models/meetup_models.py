from datetime import datetime
from .base_models import BaseModels

meetups = []

class MeetupModel(BaseModels):

    def __init__(self, location=None, happeningOn=None, tags=None, images=None, topic=None, createdBy=None, venue=None,time=None):
        self.meetup_id = len(meetups) + 1
        self.createdOn = datetime.now(),
        self.createdBy = createdBy,
        self.location = location ,
        self.images = images,
        self.topic = topic ,
        self.happeningOn = happeningOn ,
        self.tags = tags ,
        self.venue = venue ,
        self.time = time ,
        
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