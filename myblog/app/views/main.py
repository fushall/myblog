from models.article import Article
from flask import render_template, request, jsonify
from flask.blueprints import Blueprint

blueprint = Blueprint('main', __name__)


@blueprint.route('/')
def index():
    context = {
        'article_list': Article.query.all()
    }
    return render_template('main/index.html', **context)


@blueprint.route('/article/<int:article_id>')
def article(article_id):
    context = {
        'article': Article.query.get(article_id)
    }
    return render_template('main/article.html', **context)


@blueprint.route('/test', methods=['POST', 'GET'])
def test():
    if request.method == 'POST':
        import json
        x = json.loads(request.data.decode())
        return str(request.json)
    return jsonify({'a': 1}),404
