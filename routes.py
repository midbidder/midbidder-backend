from flask import Flask
app = Flask(__name__)
from routes import configure_routes
configure_routes(app)