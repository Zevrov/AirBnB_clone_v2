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

if __name__ == '__main__':
    application.run(host='0.0.0.0', port=5000)
