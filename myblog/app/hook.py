from flask import Flask, current_app


def register_hooks(app: Flask):

    @app.before_first_request
    def before_first_request():
        current_app.temp_post = None
