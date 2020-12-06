import os
from sqla_wrapper import SQLAlchemy

db = SQLAlchemy(os.getenv("DB_URI", "sqlite:///guessing_game.sqlite"))

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=False)
    email = db.Column(db.String, unique=True)
    #num_of_guesses = db.Column(db.Integer, unique=False)
    #games_played = db.Column(db.Integer)
