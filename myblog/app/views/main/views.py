from . import blueprint

from flask import render_template, g


@blueprint.route('/')
def index():

    return render_template('main/index.html')

