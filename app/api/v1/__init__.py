from flask import Blueprint, Flask
from flask_restful import Api
from .views.main_views import Home
from .views.meetup_views import Meetup
from .views.auth import User, UserLogin
from .views.question_views import QuestionView, DownvoteView, UpvoteView



version1 = Blueprint('apiv1',
                     __name__,
                     url_prefix='/api/v1')


api = Api(version1)

# home endpoints
api.add_resource(Home, '/', '/home')

# home user
api.add_resource(User,'/auth')
api.add_resource(UserLogin,'/login')


# meetup endpoints
api.add_resource(Meetup,'/meetup')

# question endpoints
api.add_resource(QuestionView,'/question')
api.add_resource(DownvoteView,'/question/downvote/<int:id>')
api.add_resource(UpvoteView,'/question/upvote/<int:id>')
