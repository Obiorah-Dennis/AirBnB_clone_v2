#!/usr/bin/python3
""" create a web application that listen in port 5000
"""


from flask import Flask, escape, render_template
from models import storage
import shlex

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


@app.route('/states_list')
def call_States():
    """ call the states created
    """
    lista = []
    dic = storage.all("State")
    for elem in dic:
        var = dic[elem].name + "/" + dic[elem].id
        lista.append(var)
    lista.sort()
    # list of ordered tuples
    lista2 = []
    for elem in lista:
        elem = elem.replace('/', ' ')
        elem = shlex.split(elem)
        lista2.append((elem[0], elem[1]))
    return (render_template('7-states_list.html', tupla=lista2))


@app.teardown_appcontext
def close(var=None):
    """ realizae this, when the process finishes
    """
    storage.close()


if __name__ == "__main__":
    # config the run
    app.run(host='0.0.0.0', port=5000)
