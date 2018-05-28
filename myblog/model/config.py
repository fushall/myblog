from . import db


class ConfigModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    blog_name = db.Column(db.Unicode(64), default='博客的名字')
    blog_owner = db.Column(db.Unicode(16), default='博主的名字')
