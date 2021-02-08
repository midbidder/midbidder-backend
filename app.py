from flask import Flask
from flask_cors import CORS
from routes import configure_routes

app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})

configure_routes(app)

