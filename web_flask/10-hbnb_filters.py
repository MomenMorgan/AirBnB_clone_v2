#!/usr/bin/python3
"""List of states on HTML states_list"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def cities_by_states():
    """display a HTML page: (inside the tag BODY)"""
    slist = sorted(storage.all(
        State).values(), key=lambda x: x.name)
    for s in slist:
        s.cities.sort(key=lambda x: x.name)

    amenity = sorted(storage.all(
        Amenity).values(), key=lambda x: x.name)
    print(amenity)
    return render_template("10-hbnb_filters.html", states=slist, amenity=amenity)


@app.teardown_appcontext
def terminate(exc):
    """close the storage"""
    storage.close()


if __name__ == '__main__':
    """start the server"""
    app.run(host='0.0.0.0', port=5000)
