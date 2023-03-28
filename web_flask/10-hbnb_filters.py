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
from models.amenity import Amenity

app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def show_filters():
    """ displays a HTML page with the list of all filters"""
    return render_template('10-hbnb_filters.html', states=storage.all(State),
                           amenities=storage.all(Amenity)


@app.teardown_appcontext
def teardown(response_or_exc):
    """ removes the current SQLAlchemy Session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
