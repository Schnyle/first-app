from app import app
from models import db, Game

with app.app_context():
    Game.query.delete()

    starting_position = Game(
        pieces = '''
            RHBQKBHR
            PPPPPPPP
            EEEEEEEE
            EEEEEEEE
            EEEEEEEE
            EEEEEEEE
            PPPPPPPP
            RHBQKBHR
        ''',
        colors = '''
            BBBBBBBB
            BBBBBBBB
            EEEEEEEE
            EEEEEEEE
            EEEEEEEE
            EEEEEEEE
            WWWWWWWW
            WWWWWWWW
        ''',
        whites_turn = True
    )

    db.session.add(starting_position)
    db.session.commit()