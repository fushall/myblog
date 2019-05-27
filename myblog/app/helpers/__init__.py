from app.helpers.login import user_logined

flask_app = None


def register_helpers(app):
    global flask_app
    flask_app = app

    app.context_processor(lambda: {
        'user_logined': user_logined
    })
