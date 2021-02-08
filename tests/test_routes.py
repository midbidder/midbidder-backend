import sys
from flask import Flask
sys.path.append('.')
from app import configure_routes
import json


def test_hello_world():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/'

    response = client.get(url)
    print(response.get_data())
    assert response.get_data() == b'Hello, World!'
    assert response.status_code == 200


def test_404():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/404'

    response = client.get(url)
    print(response.get_data())
    assert response.get_data() == b'404'
    assert response.status_code == 200
