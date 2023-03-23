from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def my_message(message):
    print('Відправлене повідомлення: ' + message)
    socketio.send(message, broadcast=True)

if __name__ == '__main__':
    socketio.run(app)
