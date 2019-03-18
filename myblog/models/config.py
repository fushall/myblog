from . import db


class ConfigModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.UnicodeText)
    value = db.Column(db.UnicodeText)
