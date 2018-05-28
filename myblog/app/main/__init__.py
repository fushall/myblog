from flask import Blueprint

blueprint = Blueprint('main', __name__)

from . import views
