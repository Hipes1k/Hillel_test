from flask import Flask
from mailsgenerator import make_dict
from height_weight import result

app = Flask(__name__)

@app.route('/generate-users/')
def index():
    return make_dict()

@app.route('/mean/')
def about():
    return result

if __name__ == '__main__':
    app.run(debug=True)
