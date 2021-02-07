from flask import Flask
from flask import request
import logging

app = Flask(__name__)
app.logger.setLevel(logging.INFO)

def configure_routes(app):
    @app.route('/', methods=['GET'])
    def hello_world():
        app.logger.info("This is the home page")
        return 'Hello, World!!'

    @app.route('/404')
    def route_404():
        return '404'
    
    @app.route('/signin', methods=['POST'])
    def sign_in():
        app.logger.info(request.to_json())
        app.logger.info("Hello")
        google_user = request.args.get('tokenId')
        return "hello"

    if __name__ == "__main__":
        app.run(debug=True, port=5000)

configure_routes(app)
app.run()