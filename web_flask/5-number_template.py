#!/usr/bin/python3
"""starts a flask web app"""

from flask import Flask

application = Flask(__name__)


@application.route('/', strict_slashes=False)
def hello_world():
    """prints hello_world"""
    return "Hello HBNB!"


@application.route('/hbnb', strict_slashes=False)
def hbnb():
    """prints hbnb"""
    return "HBNB"


@application.route('/c/<text>', strict_slashes=False)
def c(text):
    """first function with a variable"""
    return 'C ' + text.replace('_', ' ')


@application.route('/python/')
@application.route('/python/<text>')
def python(text='is cool'):
    """like the one on line 21, but with 'python' instead of 'c'"""
    return 'Python ' + text.replace('_', ' ')


@application.route('/number/<int:n>')
def number(n):
    """Returns numbers if they are ints"""
    return "{} is a number".format(n)


@application.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """display 5-number_template.html if number is an int"""
    return flask.render_template('5-number.html', title='HBNB', number=n)

if __name__ == '__main__':
    application.run(host='0.0.0.0', port=5000)
