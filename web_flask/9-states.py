#!/usr/bin/python3
"""starts a flask web app"""

from models import storage
from flask import Flask
from flask import render_template

application = Flask(__name__)
application.url_map.strict_slashes = False


@application.teardown_appcontext
def teardown_appcontext(self):
    """close and reload the storage between requests"""
    storage.close()


@application.route('/states')
def states():
    """injects states into html"""
    states = storage.all('State')
    return render_template('9-states.html', state=states)


@application.route('/states/<id>')
def state_id_list(id):
    """fill html with states and cities based on id"""
    states = storage.all('State')
    if not ("State.{}".format(id)) in states:
        state = "None"
    else:
        state = states.get("State." + id)
    return render_template('9-states.html', state=state)

if __name__ == '__main__':
    application.run(host='0.0.0.0', port=5000)
