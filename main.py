from flask import Flask, request, make_response, render_template, flash, redirect, url_for
import random
from models import db, User

app = Flask(__name__)
app.secret_key = "secret-key"

#creates all models
db.create_all()

@app.route("/", methods=["GET"])
def index():
    email = request.cookies.get("email")
    user= None

    if email:
        user = db.query(User).filter_by(email=email).first()
        return render_template("game.html", user=user)
    return render_template("index.html")


@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    email = request.form.get("email")
    user = User(name=username, email=email)
    db.add(user)
    db.commit()

    response = make_response(render_template("index.html"))
    response.set_cookie("username", username)
    response.set_cookie("email", email)
    return response

@app.route("/result", methods=["GET", "POST"])
def result():
    secret_number = random.randint(1, 30)
    guess = int(request.form.get("guess"))
    if guess == secret_number:
        message = "Congratulations! The secret number was {secret_number}"
        flash(message)
    elif guess < secret_number:
        message = "Higher"
        flash(message)
    else:
        message = "Lower"
        flash(message)
    return render_template("game.html", message=message)