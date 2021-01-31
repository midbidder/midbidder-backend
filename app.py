from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)
    
@app.route('/play')
def play():
    # create get method that sends current game's data and schedule of game
    # create post method that takes in bid
    return

@app.route('/404')
def route_404():
    return '404'