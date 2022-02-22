from flask import Flask
from flask_socketio import SocketIO, send
import threading

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'

socketIo = SocketIO(app, cors_allowed_origins='*')

app.debug = True

app.host = 'localhost'


MESSAGE = ""

def setInterval(func,time):
    e = threading.Event()
    while not e.wait(time):
        func()

def sendMessage():
    socketIo.emit("message", MESSAGE)

@socketIo.on("message")
def handleMessage(msg):
    # print(msg)
    # socketIo.emit("message", msg)
    global MESSAGE
    MESSAGE = msg
    setInterval(sendMessage, 2)
    
    return None
if __name__ == '__main__':
    socketIo.run(app)