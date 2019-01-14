from flask import Blueprint, Flask
from flask_restful import Api
from .views.main_views import Home
from .views.meetup_views import Meetup
from .views.auth import User


version1 = Blueprint('apiv1',
                     __name__,
                     url_prefix='/api/v1')


api = Api(version1)


api.add_resource(Home, '/', '/home')
api.add_resource(User,'/auth')
api.add_resource(Meetup,'/meetup')
