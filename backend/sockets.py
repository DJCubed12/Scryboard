"""Flask SocketIO endponts."""

from flask import Blueprint
from flask_socketio import SocketIO, emit

socketio_bp = Blueprint('socketio_bp', __name__)
socketio = SocketIO(logger=True, engineio_logger=True)

@socketio.on('connect')
def handle_connect():
    print('Client connected!')
    emit('message', {'data': 'Connected to server'})

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')
    
@socketio.on('client_message')
def handle_message(data):
    print('Received message:', data)
    emit('message', {'data': 'Message received: ' + data['message']})

@socketio.on('connect_error')
def handle_connect_error(data):
    print(f"The connection failed! {data}")

def sendCardUpdate(data): 
    socketio.emit('cardUpdate', {'data': data})

