#mLab login
from mLabpassword import username, password

#flask setup
from flask import Flask, render_template, redirect
app = Flask(__name__)

#Mongo DB connection with mLab
from pymongo import MongoClient

client = MongoClient("mongodb://%s:%s@ds143707.mlab.com:43707/heroku_4f1hr8cl" % (username, password))

db = client.heroku_4f1hr8cl

collection = db.mars_scrape

# scrape function
from scrape_mars import scrape

@app.route("/")
def home():
    scrape_dict = collection.find_one()
    return render_template("index.html", dict=scrape_dict)

@app.route("/scrape")
def reload():
    mars_dict = scrape()
    collection.update({"id": 1}, {"$set": mars_dict}, upsert = True)
    return redirect("http://localhost:5000/", code=302)

if __name__ == '__main__':
    app.run(debug=True)

