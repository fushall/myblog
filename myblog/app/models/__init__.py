from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class DBMixin:
    def save(self):
        db.session.add(self)
        db.session.commit()
        return self


