from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Mixin:
    def save(self):
        db.session.add(self)
        db.session.commit()
        return self

    def add(self):
        db.session.add(self)
        return self

    def delete(self):
        db.session.delete(self)
        return self

    def commit(self):
        db.session.commit()
        return self


def drop_all(app):
    with app.app_context():
        db.drop_all()


def create_all(app):
    with app.app_context():
        db.create_all()

