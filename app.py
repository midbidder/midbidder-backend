from flask import Flask

app = Flask(_name_)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/404')
def route_404():
    return '404'