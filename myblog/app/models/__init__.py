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

    def commit(self):
        db.session.commit()
        return self

