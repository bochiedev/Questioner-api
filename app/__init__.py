from flask import Flask
from app.api.v1.views.main_views import version1 as v1
from instance.config import app_config

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(app_config)

    app.register_blueprint(v1)

    return app
