from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def handle_connect():
    print('Successful Connection')
    send('Hello World!')

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)
