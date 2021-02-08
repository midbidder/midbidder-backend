from flask import Flask, request
import logging
from flask_cors import CORS
from dotenv import load_dotenv
import os
from google.oauth2 import id_token
from google.auth.transport import requests

app = Flask(__name__)
app.logger.setLevel(logging.INFO)
cors = CORS(app, resources={r"*": {"origins": "*"}})
load_dotenv()


def configure_routes(app):
    @app.route('/', methods=['GET'])
    def hello_world():
        app.logger.info("This is the home page")
        return 'Hello, World!!'

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

    if __name__ == "__main__":
        app.run(debug=True, port=5000)

configure_routes(app)
app.run()