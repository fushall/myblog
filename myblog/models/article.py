from . import db





class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Unicode, nullable=False)
    title_type = db.Column(db.UnicodeText(32))
    abstract = db.Column(db.Unicode)
    abstract_type = db.Column(db.UnicodeText(32))
    text = db.Column(db.Unicode)
    text_type = db.Column(db.UnicodeText(32))
    visible = db.Column(db.Boolean)
    accessible = db.Column(db.Boolean)
    create_at = db.Column(db.DateTime)
