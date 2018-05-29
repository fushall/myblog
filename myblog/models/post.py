from datetime import datetime

from . import db, Mixin


class PostModel(db.Model, Mixin):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Unicode(128))              # 博客标题
    summary_html = db.Column(db.UnicodeText)        # 概述/摘要
    maintext_html = db.Column(db.UnicodeText)       # markdown 转换成 html 后
    raw_markdown = db.Column(db.UnicodeText)        # 原始markdown

    posted_at = db.Column(db.DateTime, default=datetime.now())    # 发帖时间/发表于
    updated_at = db.Column(db.DateTime, default=datetime.now())   # 更新时间/更新于

    hidden = db.Column(db.Boolean, default=False)   # 对外隐藏

    @classmethod
    def create(cls, title='', markdown=''):
        html = markdown
        summary = markdown

        post = cls(
            title=title,
            summary=summary,
            html=html,
            markdown=markdown
        )
        return post.save()





