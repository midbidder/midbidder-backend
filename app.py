from flask import Flask

app = Flask(__name__)


def configure_routes(app):
  @app.route('/')
  def hello_world():
      return 'Hello, World!'

  @app.route('/404')
  def route_404():
      return '404'

  if __name__ == "__main__":
    app.run(debug=True)