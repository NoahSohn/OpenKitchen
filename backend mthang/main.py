import os
from flask import Flask, request
from flask import jsonify


from pymongo import MongoClient
from pymongo.server_api import ServerApi
import contents
from dotenv import load_dotenv

load_dotenv()

MONGODBKEY = os.getenv('MONGODBKEY')
print(MONGODBKEY)
dbclient = MongoClient(MONGODBKEY,server_api=ServerApi('1'))
dbdatabase = dbclient["openkitchen_posts"]
dbmain = dbdatabase.main

try:
    dbclient.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

app = Flask(__name__)

@app.route('/query', methods=['GET'])
def getfile():
    filenum = ""
    filenum = request.args["fileid"]
    if filenum == None:
        filenum = "404 fileid not found"
    retrivedfile = ""
    retrivedfile = dbmain.find_one({"_id":filenum})
    if retrivedfile == None:
        retrivedfile = "404 fileid not found"
    retrivedfile['_id'] = str(retrivedfile['_id'])
    print(retrivedfile)
    outputfile = jsonify(retrivedfile)
    return retrivedfile

@app.route('/query', methods=['POST'])
def createf():
    return None

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

