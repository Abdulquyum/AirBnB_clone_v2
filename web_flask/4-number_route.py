#!/usr/bin/python3
""" /c/<text>: display “C ” followed by the value of the text """

from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def slash():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb_slash():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def text_slash(text):
    return f"C {text.replace('_', ' ')}"


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_slash(text='is cool'):
    return f"Python {text.replace('_', ' ')}"


@app.route('/number/<n>', strict_slashes=False)
def n_is_number(n):
    if isinstance(n, int):
        return f"{n} is a number"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
