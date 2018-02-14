from pymongo import MongoClient
import pprint
import json

#mLab login
from mLabpassword import username, password

client = MongoClient("mongodb://%s:%s@ds143707.mlab.com:43707/heroku_4f1hr8cl" % (username, password))

db = client.heroku_4f1hr8cl

collection = db.mars_scrape

count = collection.count()

print(count)