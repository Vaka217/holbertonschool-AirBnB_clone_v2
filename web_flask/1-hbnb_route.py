#!/usr/bin/python3
""" starts a Flask web application:
Its listening on 0.0.0.0, port 5000
Routes:
/: display “Hello HBNB!”
/hbnb: display “HBNB”
"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_flask():
    """ displays 'Hello HBNB!'"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def print_hbnb():
    """ displays 'HBNB'"""
    return "HBNB"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
