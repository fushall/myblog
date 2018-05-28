from flask import Flask
from flask_login import LoginManager

from config import init_configs
from model import db
from model.user import get_user
from ext.library import LibraryManager
from ext.message import Message


def register_blueprints(app):
    from app.main import blueprint as main
    app.register_blueprint(main)

    from app.admin import blueprint as admin
    app.register_blueprint(admin)


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
    from . import library
    LibraryManager(app, library)

    # exts.message
    Message(app)

    # blueprints.
    register_blueprints(app)

    return app
