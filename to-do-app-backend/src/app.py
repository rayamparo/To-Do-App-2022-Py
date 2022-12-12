from flask import Flask, Response
from flask_cors import CORS

app = Flask(__name__, static_url_path='')
CORS(app)

@app.route('/')
def welcome_test():
    #Test if route is working
    return Response('Running on PORT: 5000')