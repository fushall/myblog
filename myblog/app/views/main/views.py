from . import blueprint

from flask import render_template


@blueprint.route('/')
def index():
    return render_template('main/index.html')

