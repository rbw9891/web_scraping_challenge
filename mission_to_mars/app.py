from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)


@app.route("/")
def index():
    mars_doc = mongo.db.mars_info.find_one()
    return render_template("index.html", mars_info=mars_doc)


# set our path to /scrape
@app.route("/scrape")
def scraper():

    # collection variable
    mars = mongo.db.mars_info

    # run scrape
    mars_data = scrape_mars.scrape()

    mars.update_one({}, {"$set": mars_data}, upsert=True)

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
