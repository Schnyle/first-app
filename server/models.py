from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class Move(db.Model, SerializerMixin):
    __tablename__ = 'moves'

    id = db.Column(db.Integer, primary_key=True)
    pieces = db.Column(db.String)
    colors = db.Column(db.String)
    whites_turn = db.Column(db.Boolean)
    fromIndex = db.Column(db.Integer)
    toIndex = db.Column(db.Integer)
    white_can_castle_long = db.Column(db.Boolean)
    white_can_castle_short = db.Column(db.Boolean)
    black_can_castle_long = db.Column(db.Boolean)
    black_can_castle_short = db.Column(db.Boolean)