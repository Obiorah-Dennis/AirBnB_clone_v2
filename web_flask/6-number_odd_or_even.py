#!/usr/bin/python3
""" create a web application that listen in port 5000
"""


from flask import Flask, escape, render_template
app = Flask(__name__)
# condition strict_slashes=False
app.url_map.strict_slashes = False


@app.route('/')
def hello():
    """ print this message
    """
    return ("Hello HBNB!")


@app.route('/hbnb')
def no_hello():
    """ print another message
    """
    return ("HBNB")


@app.route('/c/<text>')
def C_coment(text='hola'):
    """ print a comment related to C
    """
    text = text.replace('_', ' ')
    return ("C {}".format(escape(text)))


@app.route('/python')
@app.route('/python/<text>')
def python(text='is cool'):
    """ commentary for python
    """
    text = text.replace('_', ' ')
    return ("Python {}".format(escape(text)))


@app.route('/number/<int:n>')
def integer(n):
    """ print a integer number
    """
    return ("{} is a number".format(n))


@app.route('/number_template/<int:n>')
def render(n):
    """ first render html, by default it search in templates folder
    """
    return (render_template('5-number.html', n=n))


@app.route('/number_odd_or_even/<int:n>')
def second_render(n):
    """ even or odd render
    """
    return (render_template('6-number_odd_or_even.html', n=n))


if __name__ == "__main__":
    # config the run
    app.run(host='0.0.0.0', port=5000)
