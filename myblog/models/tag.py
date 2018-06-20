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


def create_tag(tag_name):
    return TagModel(name=tag_name).save()


def get_tag_byname(tag_name):
    return TagModel.query.filter_by(name=tag_name).first()


def delete_tag_nopost():
    for tag in TagModel.query.all():
        if len(tag.posts) == 0:
            tag.delete().commit()


def get_tagnames():
    return [tag.name for tag in TagModel.query.all()]


def tags_diff(tagnames):
    '''
    标签差异分析
    '''
    new_tags = []
    repeated_tags = []

    _tagnames = get_tagnames()
    for name in tagnames:
        if name in _tagnames:
            repeated_tags.append(name)
        else:
            new_tags.append(name)
    return new_tags, repeated_tags
