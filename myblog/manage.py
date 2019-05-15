from app import create_app
from app.websocket import socketio

if __name__ == '__main__':
    app = create_app()
    socketio.run(app, debug=True, port=6060)

