from . import db


CategoryMap = db.Table(
    'category_map',
    db.Column('post_id', db.Integer, db.ForeignKey('posts.id'), primary_key=True),
    db.Column('category_id', db.Integer, db.ForeignKey('categories.id'), primary_key=True)
)


class CategoryModel(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode(40), nullable=False)

    posts = db.relationship('PostModel', secondary=CategoryMap, backref=db.backref('CategoryModel', uselist=False))
