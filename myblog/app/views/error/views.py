from . import blueprint

from flask import render_template, g


@blueprint.route('/')
def index():
    print(g.static_folder)
    return '共注册了x个错误页面'


@blueprint.app_errorhandler(404)
def error_404(e):
    print(e)
    return render_template('error/404.html'), 404
