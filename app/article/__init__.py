from flask import request, jsonify

from app import user_logined
from app.models.article import Article
from app.utils import Blueprint

blueprint = Blueprint('article', __name__)


@blueprint.route('/')
def index():
    context = {
        'article_list': Article.query.all()
    }
    return blueprint.render_template('index.html', **context)


@blueprint.route('/articles')
def all_articles():
    return Article.get_all()


@blueprint.route('/articles/<string:aid>', endpoint='article', methods=['GET', 'POST', 'DELETE'])
def article(aid):
    context = {
        'article': Article.query.get(aid)
    }
    if request.method == 'GET':
        if request.args.get('api'):
            if context['article']:
                return jsonify({
                    'title': context['article'].title,
                    'abstract': context['article'].abstract,
                    'text': context['article'].text
                })
            else:
                return ({'message': '获取失败'}), 503
        else:
            return blueprint.render_template('article.html', **context)

    if request.method == 'DELETE':
        if context['article']:
            # 没登陆，则假删
            if user_logined():
                context['article'].delete()
            return '', 204
        else:
            return jsonify({'message:' '删除失败'}), 503
