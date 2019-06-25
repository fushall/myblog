from datetime import datetime

from . import db, DataBaseMixin


class Article(db.Model, DataBaseMixin):
    __tablename__ = 'article'

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

    @classmethod
    def create(cls, title, title_type='HTML', abstract='', abstract_type='HTML', text='', text_type='HTML',
               visible=True, accessible=True, create_at=None):
        obj = cls(title=title,
                  title_type=title_type,
                  abstract=abstract,
                  abstract_type=abstract_type,
                  text=text,
                  text_type=text_type,
                  visible=visible,
                  accessible=accessible,
                  create_at=create_at or datetime.now())
        obj.save()

    @classmethod
    def get_by_id(cls, aid):
        return cls.query.get(aid)

    @classmethod
    def get_all(cls):
        return cls.query.all()
