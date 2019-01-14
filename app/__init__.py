from flask import Flask
from instance.config import app_config
from app.api.v1 import version1 as v1

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(app_config)

    app.register_blueprint(v1)

    return app
