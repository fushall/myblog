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


def tagmaker(fileurl):
    if fileurl.endswith('.css'):
        tag = StyleTag(fileurl)
    elif fileurl.endswith('.js'):
        tag = ScriptTag(fileurl)
    else:
        tag = DivTag(fileurl)
    return tag
