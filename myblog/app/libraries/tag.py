from flask import Markup


class Tag:
    def __call__(self):
        raise AttributeError('请派生后调用')


class DivTag(Tag):
    def __init__(self, content):
        self.content = content

    def __call__(self):
        return Markup(f'<div>{self.content}</div>')


class ScriptTag(Tag):
    def __init__(self, src):
        self.src = src

    def __call__(self):
        return Markup(f'<script type="text/javascript" src="{self.src}"></script>')


class StyleTag(Tag):
    def __init__(self, href):
        self.href = href

    def __call__(self):
        return Markup(f'<link href="{self.href}" rel="stylesheet">')


def tagmaker(url_of_file):
    if url_of_file.endswith('.css'):
        tag = StyleTag(url_of_file)

    elif url_of_file.endswith('.js'):
        tag = ScriptTag(url_of_file)

    else:
        tag = DivTag(url_of_file)

    return tag
