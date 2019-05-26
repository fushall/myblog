from flask_sockets import Sockets

flask_app = None
sockets = Sockets()


def register_websocket(app):
    global flask_app
    flask_app = app
    sockets.init_app(flask_app)


@sockets.route('/gaga')
def gaga():
    pass
