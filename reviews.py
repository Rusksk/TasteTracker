
from flask import Blueprint, request, redirect, session
from database import get_db

reviews_bp = Blueprint("reviews", __name__)

@reviews_bp.route("/add", methods=["POST"])
def add():
    if "user_id" not in session:
        return redirect("/login")
    db = get_db()
    db.execute(
        "INSERT INTO reviews (restaurant,rating,user_id) VALUES (?,?,?)",
        (request.form["restaurant"], request.form["rating"], session["user_id"])
    )
    db.commit()
    return redirect("/")
