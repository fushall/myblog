from flask import Blueprint

blueprint = Blueprint('article', __name__)


@blueprint.route('/articles', endpoint='all_articles')
@blueprint.route('/articles/<string:aid>', endpoint='article')
def article(aid=None):
    return get_article(aid)


def get_article(aid):
    pass
