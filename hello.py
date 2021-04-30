from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'

@app.route('/json_text')
def json_text():
    return {'prediction' : .05}

# @app.route('/json_text')
