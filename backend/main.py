#importing librarys and shit
import os
from flask import Flask, request
from flask import jsonify

import certifi

from pymongo import MongoClient
from pymongo.server_api import ServerApi
from bson.objectid import ObjectId

#for some reason micah says we need this, IMO we should just commit the api keys
from dotenv import load_dotenv

load_dotenv()

MONGODBKEY = os.getenv('MONGODBKEY')
print(MONGODBKEY)

#initing the mongodb thing
dbclient = MongoClient(MONGODBKEY,server_api=ServerApi('1'), tlsCAFile=certifi.where())
dbdatabase = dbclient["openkitchen_posts"]
dbmain = dbdatabase.main

#it working? good, if not, fuck
try:
    dbclient.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

#i dunno what this does but all the examples have it
app = Flask(__name__)

#this is bad but im also bad so its all good
#it takes in an entry id and spits out the corresponding entry
@app.route('/query', methods=['GET'])
def getfile():
    filenum = ""
    filenum = request.args["fileid"]
    if filenum == None:
        filenum = "404 fileid not found"
    retrivedfile = ""
    retrivedfile = dbmain.find_one({"_id":ObjectId(filenum)})
    if retrivedfile == None:
        retrivedfile = "404 fileid not found"
    else:
        print(retrivedfile)
        retrivedfile['_id'] = str(retrivedfile['_id'])
    print(retrivedfile)
    outputfile = jsonify(retrivedfile)
    return outputfile 

#this will make a new file with an author and a title
@app.route('/query', methods=['POST'])
def createfile():
    return None

@app.route('/update', methods=['PATCH'])
def updatefile():
    filenum = ""
    filenum = request.args["fileid"]
    if filenum == None:
        filenum = "404 fileid not found"

    data = ""
    data = request.args["data"]
    if data == None:
        print("404 fileid not found")
    print(data)
    filter = {"_id":ObjectId(filenum)}
    newvalues = { "$set": {'body': data}}
    dbmain.update_one(filter, newvalues)
    return ("U did it penis brain", 202, {})

#this allows the site to be open without shitting itself
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

