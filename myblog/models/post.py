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


def parse_markdown_post(markdown_file):
    title, tags, maintext, summary = '', '', [], []
    over_summary = False
    for line in markdown_file.readlines():
        line = line.decode()
        if tags and title:
            maintext.append(line)
            if over_summary is not True:
                summary.append(line)
        if line.startswith('tags:'):
            tags = line[len('tags:'):].strip()
        elif line.startswith('title:'):
            title = line[len('title:'):].strip()
        elif line.startswith('#'):
            over_summary = True
    # 去空
    tags = [t for t in tags.split(' ') if len(t)]
    summary = ''.join(summary[:-1])
    maintext = ''.join(maintext)
    return title, tags, summary, maintext


def create_post(markdown_file, temporary=False):
    title, tags, md_summary, md_maintext = parse_markdown_post(markdown_file)
    # 怎么设计文章的临时存储？？？？

def replace_post():
    pass


def delete_post():
    pass
