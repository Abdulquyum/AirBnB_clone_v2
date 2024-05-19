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
def text_slash():
    return f"C {text.replace('_', ' ')}"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
