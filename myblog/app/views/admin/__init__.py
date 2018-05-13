from flask import Blueprint

blueprint = Blueprint('admin', __name__, template_folder='templates', url_prefix='/admin')
