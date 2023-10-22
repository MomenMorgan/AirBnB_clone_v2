#!/usr/bin/python3


""" starts a Flask web application 4 routs"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_fun(text):
    text = text.replace("_", " ")
    return "C {}".format(text)


# @app.route('/python/')
@app.route('/python/<text>', strict_slashes=False)
def python(text="is cool"):
    text = text.replace("_", " ")
    return "python {}".format(text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
