from flask import request, redirect, url_for, session

from app import user_logined
from app.models.article import Article
from app.utils import Blueprint

blueprint = Blueprint('admin', __name__, url_prefix='/admin')


@blueprint.route('/')
def index():
    context = {
        'article_list': Article.query.all()
    }
    return blueprint.render_template('index.html', **context)


@blueprint.route('/editor')
def editor():
    return blueprint.render_template('editor.html')


@blueprint.route('/editor/<string:article_id>', methods=['GET', 'POST'])
def edit_article(article_id):
    article = Article.query.get(int(article_id))
    if request.method == 'GET':
        if article:
            return blueprint.render_template('editor.html', article=article)

    elif request.method == 'POST':
        if article:
            if user_logined():
                article.title = request.form['title']
                article.abstract = request.form['abstract']
                article.text = request.form['text']
                article.save()
            return blueprint.render_template('editor.html', article=article)
    return redirect(url_for('admin.index'))


@blueprint.route('/articles', methods=['GET', 'POST'])
def create_article():
    if request.method == 'POST':
        title = request.form.get('title')
        abstract = request.form.get('abstract')
        text = request.form.get('text')
        if user_logined():
            Article.create(title=title, abstract=abstract, text=text)
        return redirect(url_for('admin.index'))


@blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        session['username'] = username
        session['password'] = password
    if request.method == 'GET':
        return blueprint.render_template('login.html')
    return redirect(url_for('admin.index'))


@blueprint.route('/logout')
def logout():
    session.pop('username')
    session.pop('password')
    return redirect(url_for('admin.index'))
