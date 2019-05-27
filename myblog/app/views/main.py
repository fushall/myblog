from models.articles import Articles
from flask import render_template, request, jsonify
from flask.blueprints import Blueprint

blueprint = Blueprint('main', __name__)


@blueprint.route('/')
def index():
    #print(request.user_logined)
    context = {
        'article_list': Articles.query.all()
    }
    return render_template('main/index.html', **context)


@blueprint.route('/articles/<int:article_id>')
def article(article_id):
    context = {
        'article': Articles.query.get(article_id)
    }
    return render_template('main/article.html', **context)


@blueprint.route('/websocket')
def websocket():
    return render_template('main/websocket.html')
