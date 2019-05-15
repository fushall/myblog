from flask_socketio import emit
from . import socketio

print('555')
@socketio.on('connect', namespace='/event')
def test_event_connect():
    print('connect')
    for i in range(10):
        emit('connect', namespace='/event')



@socketio.on('disconnect', namespace='/event')
def test_event_disconnect():
    print('disconnect')
    emit('disconnect', namespace='/event')


@socketio.on('message')
def handle_message(message):
    print('received message:' + str(message))
    emit('connect', {})