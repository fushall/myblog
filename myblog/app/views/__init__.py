from . import main, admin

flask_app = None

BLUEPRINTS = (
    main.blueprint,
    admin.blueprint
)


def register_views(app):
    for bp in BLUEPRINTS:
        app.register_blueprint(bp)

    global flask_app
    flask_app = app
