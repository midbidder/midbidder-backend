from pymongo import MongoClient
import os
client = MongoClient(os.getenv('DATABASE_CONNECTION_STRING'))
db = client['midbidder_backend']

def configure_routes(app):
    @app.route('/')
    def hello_world():
        return 'Hello, World!'

    @app.route('/404')
    def route_404():
        return '404'

    if __name__ == "__main__":
        app.run(debug=True)

