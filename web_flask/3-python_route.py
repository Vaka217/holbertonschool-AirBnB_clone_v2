#!/usr/bin/python3
""" starts a Flask web application:
Its listening on 0.0.0.0, port 5000
Routes:
/: display “Hello HBNB!”
/hbnb: display “HBNB”
/c/<text>: display “C ” followed by the value of the text variable
(replace underscore _ symbols with a space )
/python/<text>: display “Python ”, followed by the value of the text variable
(replace underscore _ symbols with a space)
"""

from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_flask():
    """ displays 'Hello HBNB!'"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def print_hbnb():
    """ displays 'HBNB'"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def print_c(text):
    """ displays “C ” followed by the value of the text variable"""
    return "C {}".format(escape(text).replace('_', ' '))


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def print_python(text='is cool'):
    """ displays “Python ” followed by the value of the text variable"""
    return "Python {}".format(escape(text).replace('_', ' '))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
