from . import db, Mixin


TagMap = db.Table(
    'tag_map',
    db.Column('tag_id', db.Integer, db.ForeignKey('tags.id'), primary_key=True),
    db.Column('post_id', db.Integer, db.ForeignKey('posts.id'), primary_key=True)
)


class TagModel(db.Model, Mixin):
    __tablename__ = 'tags'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode(16))

    posts = db.relationship('PostModel', secondary=TagMap, backref='tags')
