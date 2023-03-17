from app import app
from models import db, Move

with app.app_context():
    Move.query.delete()

    starting_position = Move(
        pieces = 'RHBQKBHRPPPPPPPPEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEPPPPPPPPRHBQKBHR',
        colors = 'BBBBBBBBBBBBBBBBEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEWWWWWWWWWWWWWWWW',
        whites_turn = True,
        toIndex = None,
        fromIndex = None
    )

    db.session.add(starting_position)
    db.session.commit()