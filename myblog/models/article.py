from . import db


class ArticleModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = None


class ArticleInfoModel:
    id = None
    article_id = None
    content_type = ['html', ' markdown']


class ArticleStateModel:
    id = None
    article_id = None
    state = ['shown', 'hidden', 'draft']


class ArticleCategoryModel:
    id = None
    article_id = None
    name = ['技术分析']

