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


def get_tagnames():
    return [tag.name for tag in TagModel.query.all()]


def tags_diff(tagnames):
    '''
    标签差异分析
    '''
    new_tag = []
    repeated_tag = []

    _tagnames = get_tagnames()
    for name in tagnames:
        if name in _tagnames:
            repeated_tag.append(name)
        else:
            new_tag.append(name)
    return new_tag, repeated_tag
