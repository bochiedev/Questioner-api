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
        self.question_data = {
            "user" : 1,
            "meetup" : 2,
            "title" : "question1",
            "body" : "When is the event and where is it being held?"
        }
    def test_get_questions(self):
        """Testing getting all questions."""

        response = self.client.get('/api/v1/question')

        res = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)

    def test_create_question(self):
        """Testing posting a question."""

        response = self.client.post(
            '/api/v1/question', data=json.dumps(self.question_data), content_type='application/json')

        res = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 201)


if __name__ == '__main__':
    unittest.main()
