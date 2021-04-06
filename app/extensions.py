from flask_pymongo import pymongo
from datetime import datetime

# Setup MongoDB here
mongo = pymongo.MongoClient('mongodb://127.0.0.1:27017/')

dbx = mongo['webhook']

act1 = dbx.act1push

record = {
    "author": "jake",
    "to_branch": "staging",
    "timestamp": datetime.now()
}
act1.insert_one(record)


