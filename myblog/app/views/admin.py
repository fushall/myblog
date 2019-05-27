from flask import render_template, redirect, url_for, request, session
from flask.blueprints import Blueprint

from app.helpers import user_logined
from models.articles import Articles, create_article as create_a_article

blueprint = Blueprint('admin', __name__, url_prefix='/admin')


@blueprint.route('/')
def index():
    context = {
        'articles': Articles.query.all()
    }
    return render_template('admin/index.html', **context)


# @blueprint.route('/articles/<int:article_id>', methods=['GET'])
# def article(article_id):
#     print(article_id)
#     return render_template('admin/article_editor.html')


@blueprint.route('/article_editor')
def article_editor():
    return render_template('admin/article_editor.html')


@blueprint.route('/article_editor/<string:article_id>', methods=['GET', 'POST'])
def edit_article(article_id):
    article = Articles.query.get(int(article_id))
    if request.method == 'GET':
        if article:
            return render_template('admin/article_editor.html', article=article)

    elif request.method == 'POST':
        if article:
            if user_logined():
                article.title = request.form['title']
                article.abstract = request.form['abstract']
                article.text = request.form['text']
                article.save()
            return render_template('admin/article_editor.html', article=article)
    return redirect(url_for('admin.index'))


@blueprint.route('/articles', methods=['GET', 'POST'])
def create_article():
    if request.method == 'POST':
        title = request.form.get('title')
        abstract = request.form.get('abstract')
        text = request.form.get('text')
        if user_logined():
            create_a_article(title=title, abstract=abstract, text=text)
        return redirect(url_for('admin.index'))


@blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        session['username'] = username
        session['password'] = password
    if request.method == 'GET':
        return render_template('admin/login.html')
    return redirect(url_for('admin.index'))


@blueprint.route('/logout')
def logout():
    session.pop('username')
    session.pop('password')
    return redirect(url_for('admin.index'))
