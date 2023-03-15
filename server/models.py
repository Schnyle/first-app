from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class Game(db.Model, SerializerMixin):
    __tablenames__ = 'games'

    id = db.Column(db.Integer, primary_key=True)