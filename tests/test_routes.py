import sys
from flask import Flask
sys.path.append('.')
from app import configure_routes
import json
from flask_cors import CORS


def test_hello_world():
    app = Flask(__name__)
    cors = CORS(app, resources={r"*": {"origins": "*"}})
    configure_routes(app)
    app.run(debug=True, port=5000)
    client = app.test_client()
    url = '/'

    response = client.get(url)
    print(response.get_data())
    assert response.get_data() == b'Hello, World!'
    assert response.status_code == 200


def test_404():
    app = Flask(__name__)
    cors = CORS(app, resources={r"*": {"origins": "*"}})
    configure_routes(app)
    app.run(debug=True, port=5000)
    client = app.test_client()
    url = '/404'

    response = client.get(url)
    print(response.get_data())
    assert response.get_data() == b'404'
    assert response.status_code == 200
