# import main Flask class and request object
import os
from flask import Flask, request
from pymongo import MongoClient
from pymongo.server_api import ServerApi
import contents
from dotenv import load_dotenv

load_dotenv()

MONGODBKEY = os.getenv('MONGODBKEY')

dbclient = MongoClient(MONGODBKEY,server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    dbclient.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

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
