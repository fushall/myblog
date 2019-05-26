from jinja2.filters import do_mark_safe
from werkzeug.urls import url_unquote

flask_app = None


def register_template_filters(app):
    global flask_app
    flask_app = app

    @app.template_filter('safe_without_code')
    def safe_without_code(text):
        print(text)
        # todo 保持代码部分的完整
        return do_mark_safe(text)

    @app.template_filter('urldecode')
    def do_url_decode(value):
        return url_unquote(value)
