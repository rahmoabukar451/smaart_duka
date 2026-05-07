from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
conn = sqlite3.connect("database.db", check_same_thread=False)




app = Flask(__name__)
app.secret_key = "secret_key"

def init_db():
    with app.app_context():
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS product (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                price REAL NOT NULL,
                description TEXT
            )
        ''')
        conn.commit()
        conn.close()





@app.route("/")
def home():
    return render_template("home.html")

@app.route("/product")
def product():
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM product")
    product = cur.fetchall()

    conn.close()

    return render_template("product.html", product=product)

@app.route("/about")
def about():
    conn = sqlite3.connect("database.db")
    conn.close()
    return render_template("about.html")

@app.route("/contact")
def contact():
    conn = sqlite3.connect("database.db")
    conn.close()
    return render_template("contact.html")

if __name__ == "__main__":
    init_db()   
    app.run(debug=True) 
