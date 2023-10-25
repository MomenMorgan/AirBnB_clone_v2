#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask, render_template, redirect, url_for

from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states')
def states():
    """Get all state data"""
    data = storage.all(State)
    return render_template("9-states.html",
                           states=data)


@app.route('/states/<id>')
def states_by_id(id):
    obj = None
    notfound = True
    for state in storage.all(State).values():
        if state.id == id:
            obj = state
            notfound = False
            break
    return render_template("9-states.html", id=id,
                           state=obj, notfound=notfound)


@app.teardown_appcontext
def terminate(exc):
    """Close SQLAlchemy session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
