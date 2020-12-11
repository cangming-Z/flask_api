from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/11/')
def hello_world11():
    return '11111'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9001, debug=app.config['DEBUG'])
