from . import blueprint

from flask import render_template


@blueprint.route('/')
def index():
    return '共注册了x个错误页面'


@blueprint.app_errorhandler(404)
def error_404(e):
    print(e)
    return render_template('error/404.html'), 404
