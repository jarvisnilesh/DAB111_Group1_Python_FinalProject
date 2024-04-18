from flask import Flask, render_template
import sqlite3
from creating_database import create_db


db_name = "movie_gross.db"

create_db()

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index_links.html") 

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/data")
def data():
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM moviesdb LIMIT 22")

    movie_collection = cursor.fetchall()

    conn.close()

    return render_template("data_table.html", moviesdb=movie_collection)

if __name__=="__main__":
    app.run(debug=True)
