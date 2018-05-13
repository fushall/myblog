from app import create_app as __create_app


def create_app():
    app = __create_app()

    print(app.url_map)
    print(app.config)
    return app
