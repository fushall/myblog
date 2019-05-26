import settings
from flask import Flask

from app.template_filters import register_template_filters
from models import register_models
from .views import register_views
from .websocket import register_websocket
from .api import register_api


def create_app():
    app = Flask(__name__)

    # load config from settings.py
    app.config.from_object(settings)

    # register views and blueprints
    register_views(app)

    # register flask-sqlalchemy object
    register_models(app)

    # register flask-sockets
    register_websocket(app)

    # register template filters
    register_template_filters(app)

    # register api
    register_api(app)

    return app
