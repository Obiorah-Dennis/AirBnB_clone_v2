#!/usr/bin/python3
""" create a web application that listen in port 5000
"""


from flask import Flask, escape, render_template
from models import storage
import shlex


app = Flask(__name__)
# condition strict_slashes=False
app.url_map.strict_slashes = False


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


@app.route('/cities_by_states')
def cities_per_State():
    """ cities per states
    """
    lista = []
    dic = storage.all("State")
    for elem in dic:
        lista.append((dic[elem].id, dic[elem].name))
    lista = sorted(lista, key=lambda x: x[1])
    # list of cities
    cities = []
    for state in dic:
        aux = dic[state].cities
        for city in aux:
            cities.append((dic[state].name, city.id, city.name))
    cities = sorted(cities, key=lambda x: x[2])
    return (render_template('8-cities_by_states.html', S=lista, C=cities))


@app.route('/states')
def only_states():
    """ send all states
    """
    lista = []
    dic = storage.all('State')
    for elem in dic:
        lista.append((dic[elem].id, dic[elem].name))
    lista = sorted(lista, key=lambda x: x[1])
    return (render_template('9-states.html', S=lista, C=None, F=3))


@app.route('/states/<id>')
def city_of_state_id(id):
    """ cities of state id
    """
    lista = []
    flag = 0
    dic = storage.all('State')
    for key in dic:
        if (id == dic[key].id):
            flag = 1
            lista.append((dic[key].id, dic[key].name))
    if (flag == 0):
        return (render_template('9-states.html', S=None, C=None, F=0))
    dic = storage.all('City')
    cities = []
    for elem in dic:
        if (dic[elem].state_id == lista[0][0]):
            cities.append((dic[elem].id, dic[elem].name))
    cities = sorted(cities, key=lambda x: x[1])
    return (render_template('9-states.html', S=lista, C=cities, F=1))


@app.route('/hbnb_filters')
def hbnb():
    """ using static web page created before
    """
    states, S = [], []
    cities, C = [], []
    amenities, A = [], []
    dic = storage.all('State')
    for elem in dic:
        states.append((dic[elem].id, dic[elem].name))
    S = sorted(states, key=lambda x: x[1])
    dic = storage.all('City')
    for el in dic:
        cities.append((dic[el].id, dic[el].name, dic[el].state_id))
    C = sorted(cities, key=lambda x: x[1])
    dic = storage.all('Amenity')
    for elem in dic:
        amenities.append((dic[elem].id, dic[elem].name))
    A = sorted(amenities, key=lambda x: x[1])
    return render_template('10-hbnb_filters.html', S=S, C=C, A=A)


@app.route('/hbnb')
def hbnb_complete():
    """ using static web page created before
    """
    states, S = [], []
    cities, C = [], []
    amenities, A = [], []
    places, P = [], []
    dic = storage.all('State')
    for elem in dic:
        states.append((dic[elem].id, dic[elem].name))
    S = sorted(states, key=lambda x: x[1])
    dic = storage.all('City')
    for el in dic:
        cities.append((dic[el].id, dic[el].name, dic[el].state_id))
    C = sorted(cities, key=lambda x: x[1])
    dic = storage.all('Amenity')
    for elem in dic:
        amenities.append((dic[elem].id, dic[elem].name))
    A = sorted(amenities, key=lambda x: x[1])
    dic = storage.all('Place')
    for e in dic:
        places.append((dic[e].name, dic[e].price_by_night,
                       dic[e].max_guest, dic[e].number_rooms,
                       dic[e].number_bathrooms,
                       dic[e].user.first_name,
                       dic[e].user.last_name,
                       dic[e].description))
    P = sorted(places, key=lambda x: x[0])
    return render_template('100-hbnb.html', S=S, C=C, A=A, P=P)


@app.teardown_appcontext
def close(var=None):
    """ realizae this, when the process finishes
    """
    storage.close()


if __name__ == "__main__":
    # config the run
    app.run(host='0.0.0.0', port=5000)
