# import main Flask class and request object
import os
from flask import Flask, request
from pymongo import MongoClient
import contents
from dotenv import load_dotenv

MONGODBKEY = os.getenv('MONGODBKEY')

dbclient = MongoClient(MONGODBKEY)
db = dbclient[""]


# create the Flask app
app = Flask(__name__)

@app.route('/query-example')
def query_example():
    return 'Query String Example'

@app.route('/form-example')
def form_example():
    return 'Form Data Example'

@app.route('/json-example')
def json_example():
    return 'JSON Object Example'

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)
