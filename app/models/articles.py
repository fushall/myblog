from datetime import datetime

from . import db, DataBaseMixin


class Articles(db.Model, DataBaseMixin):
    __tablename__ = 'articles'

    id = db.Column(db.Integer, db.Sequence('article_id_seq'), primary_key=True)
    title = db.Column(db.Unicode, nullable=False)
    title_type = db.Column(db.UnicodeText(32))
    abstract = db.Column(db.Unicode)
    abstract_type = db.Column(db.UnicodeText(32))
    text = db.Column(db.Unicode)
    text_type = db.Column(db.UnicodeText(32))
    visible = db.Column(db.Boolean)
    accessible = db.Column(db.Boolean)
    create_at = db.Column(db.DateTime(timezone=True))


def create_article(title, title_type='HTML', abstract='', abstract_type='HTML', text='', text_type='HTML', visible=True,
                   accessible=True, create_at=None):
    article = Articles(title=title,
                       title_type=title_type,
                       abstract=abstract,
                       abstract_type=abstract_type,
                       text=text,
                       text_type=text_type,
                       visible=visible,
                       accessible=accessible,
                       create_at=create_at or datetime.now())
    article.save()

