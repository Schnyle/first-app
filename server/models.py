from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class Game(db.Model, SerializerMixin):
    __tablenames__ = 'games'

    id = db.Column(db.Integer, primary_key=True)
    pieces = db.Column(db.String)
    colors = db.Column(db.String)
    whites_turn = db.Column(db.Boolean)