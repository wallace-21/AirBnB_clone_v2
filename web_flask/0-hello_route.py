#!/usr/bin/python3

""" import flask module"""
from flask import Flask

app = Flask(__name__)

"""function that prints a string"""

@app.route('/', strict_slashes=False)


def hello_hbnb():
    return "Hello HBNB"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
