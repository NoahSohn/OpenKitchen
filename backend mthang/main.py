# importing librarys and shit
import os
from flask import Flask, request
from flask import jsonify

import certifi

from pymongo import MongoClient
from pymongo.server_api import ServerApi
from pymongo.mongo_client import MongoClient
from bson.objectid import ObjectId
import pymongo

# for some reason micah says we need this, IMO we should just commit the api keys
from dotenv import load_dotenv

load_dotenv()

MONGODBKEY = os.getenv('MONGODBKEY')
print(MONGODBKEY)

# initing the mongodb thing
dbclient = MongoClient(MONGODBKEY, server_api=ServerApi(
    '1'), tlsCAFile=certifi.where())
dbdatabase = dbclient["openkitchen_posts"]
dbmain = dbdatabase.main

# it working? good, if not, fuck
try:
    dbclient.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

# i dunno what this does but all the examples have it
app = Flask(__name__)

# this is bad but im also bad so its all good
# it takes in an entry id and spits out the corresponding entry


@app.route('/query', methods=['GET'])
def getfile():
    filenum = ""
    filenum = request.args["fileid"]
    if filenum == None:
        filenum = "404 fileid not found"
    retrivedfile = ""
    retrivedfile = dbmain.find_one({"_id": ObjectId(filenum)})
    if retrivedfile == None:
        retrivedfile = "404 fileid not found"
    else:
        print(retrivedfile)
        retrivedfile['_id'] = str(retrivedfile['_id'])
    print(retrivedfile)
    return retrivedfile

@app.route('/query', methods=['DELETE'])
def delfile():
    searchterm = request.args["term"]
    if searchterm == None:
        searchterm = "_id"

    searchvalue = request.args["value"].strip()
    if searchvalue == None:
        searchvalue = "0"
    if searchterm == "_id":
        searchvalue = ObjectId(searchvalue)

    retrivedfile = dbmain.find_one({searchterm:searchvalue})
    if retrivedfile == None:
        retrivedfile = "404 fileid not found"
    else:
        print(retrivedfile)
        dbmain.delete_one({"_id" : retrivedfile["_id"]})
    return "202"

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
    filter = {"_id": ObjectId(filenum)}
    newvalues = {"$set": {'body': data}}
    dbmain.update_one(filter, newvalues)
    return ("U did it penis brain", 202, {})

@app.route('/getall', methods=['GET'])
def getfiles():
    output = []
    for x in dbmain.find():
        if "body" in x and "_id" in x and "author" in x and "title" in x:
            output.append({"_id":str(x["_id"]), "body":str(x["body"]), "author":x["author"], "title":x["title"]})
    print(output)
    return (output, 202, {})

# this allows the site to be open without shitting itself


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
