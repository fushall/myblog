from flask import Flask
from jinja2.filters import do_mark_safe
from werkzeug.urls import url_unquote

import config
from app.models import register_models
from app.utils import register_blueprints
from app.utils.login import user_logined



def create_app():
    app = Flask(__name__)

    # load config from settings.py
    app.config.from_object(config)

    # register all blueprints
    register_blueprints(app)

    # register flask-sqlalchemy object
    register_models(app)

    @app.template_filter('safe_except_code')
    def safe_without_code(text):
        # todo 保持代码部分的完整
        return do_mark_safe(text)

    @app.template_filter('urldecode')
    def do_url_decode(value):
        return url_unquote(value)

    app.context_processor(lambda: {
        'user_logined': user_logined
    })

    return app
