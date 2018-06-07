from flask import Flask, render_template


def register_errors(app: Flask):
    @app.errorhandler(404)
    def error_404(e):
        return render_template('error/404.html'), 404
