from flask import Flask


def register_blueprints(app: Flask):
    from app.main import blueprint as main
    app.register_blueprint(main)

    from app.admin import blueprint as admin
    app.register_blueprint(admin)
