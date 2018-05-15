from flask import Flask
from flask_login import LoginManager

from app.configs import init_configs
from app.views import register_views
from app.models import db
from app.models.user import get_user
from app.exts.library import LibraryManager
from app.exts.message import Message


def create_app():
    app = Flask(__name__)

    # config
    init_configs(app)

    # flask-sqlalchemy
    db.init_app(app)

    # flask-login
    login = LoginManager(app)
    login.login_message = None
    login.login_view = 'admin.login'
    login.user_loader(lambda user_id: get_user(user_id))

    # exts.library
    from . import libraries
    LibraryManager(app, libraries)

    # exts.message
    Message(app)

    # views and blueprints.
    register_views(app)

    return app
