from flask_socketio import SocketIO

flask_app = None
socketio = SocketIO()


def register_socketio(app):
    global flask_app
    flask_app = app
    socketio.init_app(flask_app)

    from . import main