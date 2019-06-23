# https://github.com/Microsoft/api-guidelines/blob/vNext/Guidelines.md#711-http-status-codes

from flask import jsonify, request
from flask.blueprints import Blueprint

from app.helpers import user_logined
from app.models import Articles

api = Blueprint('api', __name__, url_prefix='/api')
flask_app = None


def register_api(app):
    global flask_app
    flask_app = app
    app.register_blueprint(api)


@api.route('/article/<string:article_id>', methods=['GET', 'DELETE'])
def api_article(article_id):
    article = Articles.query.get(int(article_id))
    if request.method == 'DELETE':
        if article:
            if user_logined():
                article.delete()
            return '', 204
        return jsonify({'message:' '删除失败'}), 503
    elif request.method == 'GET':
        if article:
            return jsonify({
                'title': article.title,
                'abstract': article.abstract,
                'text': article.text
            })
        return ({'message': '获取失败'}), 503
