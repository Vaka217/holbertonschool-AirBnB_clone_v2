#!/usr/bin/python3
""" starts a Flask web application:
Its listening on 0.0.0.0, port 5000
Routes:
/states_list: display a HTML page: (inside the tag BODY)
H1 tag: “States”
UL tag: with the list of all State objects present in DBStorage
sorted by name (A->Z) tip
LI tag: description of one State: <state.id>: <B><state.name></B>
"""

from flask import Flask
from flask import render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def show_states():
    """ displays a HTML page with the list of all State objects in the DB"""
    return render_template('7-states_list.html', states=storage.all(State))


@app.teardown_appcontext
def teardown(response_or_exc):
    """ removes the current SQLAlchemy Session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
