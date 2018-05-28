from flask import Blueprint

blueprint = Blueprint('admin', __name__, url_prefix='/admin')

from . import views
