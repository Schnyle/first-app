from app import app
from models import db, Game

with app.app_context():
    Game.query.delete()
    