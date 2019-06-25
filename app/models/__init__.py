from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

flask_app = None


def register_models(app):
    db.init_app(app)

    global flask_app
    flask_app = app


class DataBaseMixin:

    def save(self, commit=True):
        db.session.add(self)
        if commit:
            db.session.commit()

    def delete(self, commit=True):
        db.session.delete(self)
        if commit:
            db.session.commit()
