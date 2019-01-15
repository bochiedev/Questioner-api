import unittest
from flask import json
from datetime import datetime
from app import create_app
import json


class TestQuestioner(unittest.TestCase):

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app("testing")
        self.client = self.app.test_client()
        self.meetup_data = {
            "location": "Nairobi",
            "venue": "Ihub",
            "images": [],
            "topic": "Dev Fest",
            "happeningOn": "12-2-2019",
            "time": "1800",
            "tags": ["programming", "Js"],
            "createdBy": 1,
        }
    def test_get_meetup(self):
        """Testing getting a meetup."""

        response = self.client.get('/api/v1/meetup')

        res = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)

    def test_create_meetup(self):
        """Testing posting a meetup."""

        response = self.client.post(
            '/api/v1/meetup', data=json.dumps(self.meetup_data), content_type='application/json')

        res = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 201)


if __name__ == '__main__':
    unittest.main()
