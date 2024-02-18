#!/usr/bin/python3

""" import flask module"""
from flask import Flask

app = Flask(__name__)
"""create an instance of flask"""


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ function that prints a string"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
