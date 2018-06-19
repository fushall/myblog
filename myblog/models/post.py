from datetime import datetime

from . import db, Mixin


class PostModel(db.Model, Mixin):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Unicode(128), nullable=False)  # 标题
    summary_html = db.Column(db.UnicodeText)            # 概述
    maintext_html = db.Column(db.UnicodeText)           # 正文
    raw_markdown = db.Column(db.UnicodeText)            # 原始markdown

    temporary = db.Column(db.Boolean)                   # 临时的

    posted_at = db.Column(db.DateTime, default=datetime.now())    # 发表于...
    updated_at = db.Column(db.DateTime, default=datetime.now())   # 更新于...


def create_post():
    pass


def replace_post():
    pass


def delete_post():
    pass
