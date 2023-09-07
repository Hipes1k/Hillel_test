from flask import Flask, jsonify, render_template
import requests


app = Flask(__name__)


@app.route('/requirements', methods=['GET'])
def requirements():
    with open('requirements.txt', 'rb') as file:
        requirements_content = file.read()
    return requirements_content

@app.route('/generate-users/', methods=['GET'])
def generate_users():
    return render_template('text.txt')


@app.route('/mean/', methods=['GET'])
def mean():
    return render_template('weight_height.txt')


@app.route("/space/", methods=['GET'])
def get_astrons():
    json = requests.get('http://api.open-notify.org/astros.json').json()
    return jsonify({
            "Astronauts number": json["number"]
        })

if __name__ == '__main__':
    app.run(debug=True)
