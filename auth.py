
from flask import Blueprint, request, redirect, session, render_template
from database import get_db

auth = Blueprint("auth", __name__)

@auth.route("/register", methods=["GET","POST"])
def register():
    if request.method == "POST":
        db = get_db()
        db.execute("INSERT INTO users (username,password) VALUES (?,?)",
                   (request.form["username"], request.form["password"]))
        db.commit()
        return redirect("/login")
    return render_template("register.html")

@auth.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        db = get_db()
        user = db.execute(
            "SELECT * FROM users WHERE username=? AND password=?",
            (request.form["username"], request.form["password"])
        ).fetchone()
        if user:
            session["user_id"] = user["id"]
            return redirect("/")
    return render_template("login.html")

@auth.route("/logout")
def logout():
    session.clear()
    return redirect("/")
