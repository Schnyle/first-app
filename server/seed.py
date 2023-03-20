from app import app
from models import db, Move

with app.app_context():
    Move.query.delete()

    starting_position = Move(
        pieces = 'RHBQKBHRPPPPPPPPEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEPPPPPPPPRHBQKBHR',
        colors = 'BBBBBBBBBBBBBBBBEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEWWWWWWWWWWWWWWWW',
        whites_turn = True,
        toIndex = None,
        fromIndex = None,
        white_can_castle_long = True,
        white_can_castle_short = True,
        black_can_castle_long = True,
        black_can_castle_short = True
    )

    db.session.add(starting_position)
    db.session.commit()