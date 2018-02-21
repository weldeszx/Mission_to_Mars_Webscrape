# from pymongo import MongoClient
# import pprint
# import json
from flask import Flask
import pymongo

app=Flask(__name__)
app.config['MONGO_DBNAME']='mars_mission_webscrape'
app.config['MONGO_URL']='mongodb://gw:homework@ds241668.mlab.com:41668/mars_mission_webscrape'
# mongo2=pymongo(app)
 # db = client.get_default_database()



#mLab login
# from mLabpassword import username, password

# client = MongoClient("mongodb://%s:%s@ds143707.mlab.com:43707/heroku_4f1hr8cl" % (username, password))

# db = client.heroku_4f1hr8cl

# collection = db.mars_scrape

# count = collection.count()

# print(count)
