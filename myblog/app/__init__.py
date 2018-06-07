from flask import Flask

from configs import register_configs
from .ext import register_exts
from .blueprint import register_blueprints
from .hook import register_hooks
from .error import register_errors


def create_app():
    app = Flask(__name__)

    register_configs(app)

    register_exts(app)
    register_blueprints(app)
    register_hooks(app)

    return app
