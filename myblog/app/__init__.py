import settings
from flask import Flask

from models import register_models
from .views import register_views


def create_app():
    app = Flask(__name__)

    # load config from settings.py
    app.config.from_object(settings)

    # register views and blueprints
    register_views(app)

    # register flask-sqlalchemy object
    register_models(app)

    return app
