from flask import flash, get_flashed_messages
from markupsafe import Markup


_TEMPLATE = '''
<div class="alert alert-{category} alert-dismissible fade show w-100" role="alert">
    {message}
    <button type="button" class="close" data-dismiss="alert" aria-label="Close">
      <span aria-hidden="true">&times;</span>
    </button>      
</div>
'''

_CATEGORIES = [
    'primary', 'secondary',
    'success', 'danger',
    'warning', 'info',
    'light',   'dark'
]

_DEFAULT_CATEGORY = 'danger'


class Message:
    def __init__(self, app=None):
        self.app = None
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        self.app = app
        self.app.jinja_env.globals['message'] = self

    def __call__(self):

        messages = ''
        for (cate, msg) in get_flashed_messages(with_categories=True):
            if cate == 'message':
                cate = 'warning'
            messages += _TEMPLATE.format(message=msg, category=cate)

        return Markup(messages)
