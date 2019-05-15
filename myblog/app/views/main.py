
from models.article import Article
from flask import render_template, request, jsonify
from flask.blueprints import Blueprint
from app.websocket import socketio
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
        title = request.json.get('title')
        abstract = request.json.get('abstract')
        text = request.json.get('text')
        article = Article(title=title, abstract=abstract, text=text)

    socketio.emit('connect', data={1:1})
    return jsonify({'a': 1}), 404


@blueprint.route('/websocket')
def websocket():

    return render_template('main/websocket.html')
