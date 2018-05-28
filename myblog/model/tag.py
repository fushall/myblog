from . import db


class TagModel(db.Model):
    __tablename__ = 'tags'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode(16))


TagsMapModel = db.Table(
    'tags_map',
    db.Column('tag_id', db.Integer(), db.ForeignKey('tags.id'), primary_key=True),
    db.Column('post_id', db.Integer(), db.ForeignKey('posts.id'), primary_key=True)
)

