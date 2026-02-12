
from flask import Flask, render_template
from database import get_db
from auth import auth
from reviews import reviews_bp

app = Flask(__name__)
app.secret_key = "dev"

app.register_blueprint(auth)
app.register_blueprint(reviews_bp)

@app.route("/")
def index():
    db = get_db()
    try:
        reviews = db.execute("SELECT * FROM reviews").fetchall()
    except:
        reviews = []
    return render_template("index.html", reviews=reviews)

if __name__ == "__main__":
    app.run(debug=True)
