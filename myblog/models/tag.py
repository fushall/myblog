from . import db, Mixin


TagMap = db.Table(
    'tag_map',
    db.Column('tag_id', db.Integer, db.ForeignKey('tags.id'), primary_key=True),
    db.Column('post_id', db.Integer, db.ForeignKey('posts.id'), primary_key=True)
)


class TagModel(db.Model, Mixin):
    __tablename__ = 'tags'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode(16), unique=True)

    posts = db.relationship('PostModel', secondary=TagMap, backref='tags')


def delete_tag_nopost():
    for tag in TagModel.query.all():
        if len(tag.posts) == 0:
            tag.delete().commit()


def get_tagnames():
    return [tag.name for tag in TagModel.query.all()]
