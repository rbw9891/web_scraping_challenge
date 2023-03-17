from flask import Flask, render_template
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)


@app.route("/")
def index():

    return render_template("index.html")


# set our path to /scrape
@app.route("/scrape")
def scraper():

    # create db
    mars = mongo.db.mars

    # run scrape
    mars_data = scrape_mars.scrape()

    mars.update({}, mars_data, upsert=True)


if __name__ == "__main__":
    app.run(debug=True)
