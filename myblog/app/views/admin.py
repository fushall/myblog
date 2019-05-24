from flask import render_template, redirect, url_for, request, session
from flask.blueprints import Blueprint

from models.articles import Articles, create_article as create_a_article

blueprint = Blueprint('admin', __name__, url_prefix='/admin')


@blueprint.route('/')
def index():
    context = {
        'articles': Articles.query.all()
    }
    return render_template('admin/index.html', **context)


@blueprint.route('/articles/<int:article_id>', methods=['GET'])
def article(article_id):
    print(article_id)
    return render_template('admin/article_editor.html')


@blueprint.route('/article_editor')
def article_editor():
    return render_template('admin/article_editor.html')


@blueprint.route('/articles', methods=['GET', 'POST'])
def create_article():
    if request.method == 'POST':
        title = request.form.get('title')
        abstract = request.form.get('abstract')
        text = request.form.get('text')
        create_a_article(title=title, abstract=abstract, text=text)
        return redirect(url_for('admin.index'))


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
