from flask import Flask
from app.api.v1.views.main_views import version1 as v1
from app.api.v1.views.auth import auth as auth
from app.api.v1.views.meetup_views import meetup as meetup
from instance.config import app_config

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(app_config)

    app.register_blueprint(v1)
    app.register_blueprint(auth)
    app.register_blueprint(meetup)



    return app
