from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

flask_app = None


def register_models(app):
    db.init_app(app)

    global flask_app
    flask_app = app
