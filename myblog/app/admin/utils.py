from flask import current_app

from utils import markdown2html
from models.tag import TagModel


def parse_post(markdown_file):
    title, tags, maintext, summary = '', '', [], []
    over_summary = False
    for line in markdown_file.stream.readlines():
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


def make_post_dict(new_tags, repeated_tags, title, md_summary, md_maintext):
    return dict(
        tags=dict(new=new_tags, repeated=repeated_tags),
        title=title,
        summary_html=markdown2html(md_summary),
        maintext_html=markdown2html(md_maintext),
        raw_markdown=md_maintext
    )

