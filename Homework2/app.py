from flask import Flask, jsonify
from mailsgenerator import make_dict
from height_weight import weight_height_kg_cm
from jinja2 import Template
import requests


app = Flask(__name__)


@app.route('/requirements', methods=['GET'])
def requirements():
    with open('requirements.txt', 'rb') as file:
        requirements_content = file.read()
    return requirements_content

@app.route('/generate-users/', methods=['GET'])
def generate_users():
    return Template("{{ make_dict() }}").render(make_dict=make_dict)


@app.route('/mean/', methods=['GET'])
def mean():
    return Template("{{ weight_height_kg_cm() }}").render(weight_height_kg_cm=weight_height_kg_cm)


@app.route("/space/", methods=['GET'])
def get_astrons():
    json = requests.get('http://api.open-notify.org/astros.json').json()
    return jsonify({
            "Astronauts number": json["number"]
        })

if __name__ == '__main__':
    app.run(debug=True)
