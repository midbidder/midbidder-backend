from flask import request
from pymongo import MongoClient
from google.oauth2 import id_token
from google.auth.transport import requests
import os

client = MongoClient(os.getenv('DATABASE_CONNECTION_STRING'))
db = client['midbidder_backend']

def configure_routes(app):
    @app.route('/', methods=['GET'])
    def hello_world():
        return 'Hello, World!'

    @app.route('/404')
    def route_404():
        return '404'
    
    @app.route('/signin', methods=['GET','POST', 'OPTIONS'])
    def sign_in():
        data = request.get_json()
        if(data):
            idinfo = id_token.verify_oauth2_token(data['id_token'], requests.Request(), os.getenv('FLASK_APP_GOOGLE_AUTH_CLIENT_ID'))
            userid = idinfo['sub']
            print(userid)
            return userid
        else:
            return "Did not get Data"