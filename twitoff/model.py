"""database for TwitOff"""

from flask_sqlalchemy import SQLAlchemy


DB = SQLAlchemy()

class User(DB.Model):
    id = DB.Column(DB.Integer, primary_key = True)
    username = DB.Column(DB.String(15), unique=True, nullable=False)


class Tweets(DB.Model):
    id = DB.Column(DB.Integer, primary_key = True)
    text = DB.Column(DB.Unicode(280))
