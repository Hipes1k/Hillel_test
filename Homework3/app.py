import sqlite3

from flask import Flask, request, jsonify
import json


app = Flask(__name__)


def connect_database():
    connection = sqlite3.connect('hillel.db')
    return connection


@app.route('/names/')
def get_names():
    connection = connect_database()
    customers = connection.execute("SELECT DISTINCT first_name FROM customers").fetchall()
    connection.close()
    return json.dumps([
        {
            'first_name': customer[0]
        }
        for customer in customers])


@app.route("/customers/")
def get_customers():
    dct = {}
    connection = connect_database()
    names = connection.execute("SELECT first_name, last_name FROM customers ORDER BY id DESC").fetchall()
    connection.close()
    for name in names:
        dct[name[0]] = name[1]
    args = request.args
    first_name = args.get('first_name')
    last_name = args.get('last_name')

    if None not in (first_name, last_name):
        result = {key: value for key, value in dct.items() if key == first_name and value == last_name}
    elif first_name is not None:
        result = {key: value for key, value in dct.items() if key == first_name}
    elif last_name is not None:
        result = {key: value for key, value in dct.items() if value == last_name}
    else:
        return dct

    return result


@app.route('/tracks/count')
def count_track():
    connection = connect_database()
    count = connection.execute("SELECT COUNT(id) FROM tracks").fetchone()
    connection.close()
    return jsonify({
        'Tracks Count': count[0]
    })


@app.route('/tracks/duration')
def tracks_duration():
    connection = connect_database()
    tracks = connection.execute("SELECT name, duration FROM tracks ORDER BY id ASC").fetchall()
    connection.close()
    return json.dumps([
        {
            'track_name': track[0],
            'duration': track[1]
        }
        for track in tracks
    ])


if __name__ == '__main__':
    app.run(debug=True)










