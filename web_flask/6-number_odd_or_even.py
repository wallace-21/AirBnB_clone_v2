#!/usr/bin/python3

""" import flask module"""
from flask import Flask, render_template

app = Flask(__name__)
"""create an instance of flask"""


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ function that prints a string"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    text = text.replace('_', ' ')
    return ("C {}".format(text))


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text):
    text = text.replace('_', ' ')
    return ("Python {}".format(text))


@app.route('/number/<int:n>', strict_slashes=False)
def is_it_a_number(n):
    return ("{} is a number".format(n))


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """funcion that prints numbers"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """function thaat print even or odd"""
    if isinstance(n, int):
        even_or_odd = "even" if n % 2 == 0 else "odd"
        return render_template('6-number_odd_or_even.html',
                               n=n, even_or_odd=even_or_odd)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
