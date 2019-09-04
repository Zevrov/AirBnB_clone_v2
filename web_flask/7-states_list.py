#!/usr/bin/python3
"""starts a flask web app"""

from models import storage
from flask import Flask
from flask import render_template

application = Flask(__name__)


@application.teardown_appcontext
def closeStorageAfterRequest(error):
    """close and reload the storage between requests"""
    models.storage.close()


@site.route('/states_list')
def showStates():
    """List all the stored states"""
    states = storage.all('State').values()
    return render_template('7-states_list.html', states=states)

if __name__ == '__main__':
    application.run(host='0.0.0.0', port=5000)
