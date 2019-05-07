from flask import render_template, redirect, url_for, request, session
from flask.blueprints import Blueprint

from models.article import Article

blueprint = Blueprint('admin', __name__, url_prefix='/admin')


@blueprint.route('/')
def index():
    context = {
        'articles': Article.query.all()
    }
    return render_template('admin/index.html', **context)


@blueprint.route('/new/article', methods=['GET', 'POST'])
def new_article():
    if request.method == 'POST':
        print(request.form)
    return render_template('admin/new_article.html')


@blueprint.route('/article/<int:article_id>', methods=['GET', 'POST'])
def article(article_id):
    if request.method == 'POST':
        print(request.form)
    return render_template('admin/new_article.html')


@blueprint.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'a' and password == 'a':
            session['logined'] = True
    return redirect(url_for('admin.index'))


@blueprint.route('/logout')
def logout():
    session['logined'] = False
    return redirect(url_for('admin.index'))
