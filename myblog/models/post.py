from functools import partial
from datetime import datetime

from utils import markdown2html
from . import db, Mixin
from .tag import TagModel, create_tag, get_tag_byname, tags_diff


class PostModel(db.Model, Mixin):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Unicode(128), nullable=False)  # 标题
    summary_html = db.Column(db.UnicodeText)            # 概述
    maintext_html = db.Column(db.UnicodeText)           # 正文
    raw_markdown = db.Column(db.UnicodeText)            # 原始markdown

    temporary = db.Column(db.Boolean, default=True)     # 临时的

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


def create_post(markdown_file):
    title, tags, md_summary, md_maintext = parse_markdown_post(markdown_file)
    new_tags, repeated_tags = tags_diff(tags)

    tags = []
    tags.extend([create_tag(tagname) for tagname in new_tags])
    tags.extend([get_tag_byname(tagname) for tagname in repeated_tags])

    post = PostModel(
        title=title,
        summary_html=markdown2html(md_summary),
        maintext_html=markdown2html(md_maintext),
        raw_markdown=md_maintext,
        tags=tags
    )
    return post.save()


def get_post(post_id: int):
    return PostModel.query.get(post_id)


def get_posts():
    return PostModel.query.all()


def replace_post(src_post_id, dist_post_id):
    src_post = get_post(src_post_id)
    dist_post = get_post(dist_post_id)

    dist_post.title = src_post.title
    dist_post.summary_html = src_post.summary_html
    dist_post.maintext_html = src_post.maintext_html
    dist_post.raw_markdown = src_post.raw_markdown
    dist_post.updated_at = datetime.now()

    db.session.delete(src_post)
    db.session.commit()


def delete_post(post_id):
    post = get_post(post_id)
    db.session.delete(post)
    db.session.commit()

