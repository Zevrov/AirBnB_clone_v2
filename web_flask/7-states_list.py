#!/usr/bin/python3
"""Module to start a Flask web application"""

from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown(self):
    """Closes current SQLAlchemy session after each request"""
    storage.close()


@app.route('/states_list')
def state_list():
    """Injects states and info into html"""
    states = storage.all('State')
    return render_template('7-states_list.html', state=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
