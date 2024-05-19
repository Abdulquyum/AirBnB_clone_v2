#!/usr/bin/python3
""" Starts a Flask web application
/: display “Hello HBNB!” and /hbnb: display “HBNB”
"""

from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def slash():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def slash_hbnb():
    return "HBNB"
