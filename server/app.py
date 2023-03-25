import sys
sys.path.insert(0, './chess')

from flask import Flask, jsonify, request, make_response
from flask_migrate import Migrate
from flask_restful import Api, Resource
from flask_cors import CORS

from models import db, Move
from chess import Chess

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)

api = Api(app)

@app.route('/moves', methods=['GET', 'PATCH'])
def moves():

    if request.method == 'GET':
        return make_response(
            jsonify([m.to_dict() for m in Move.query.all()]),
            200
        )
    
    if request.method == 'PATCH':
        chessState = Move.query.order_by(Move.id.desc()).first()
        chess = Chess(chessState)

        data = request.get_json()
        fromIndex = data['fromIndex']
        toIndex = data['toIndex']

        # check if valid move
        currentState = chess.state_dict.copy()
        newState = chess.move(fromIndex, toIndex)

        # if invalid move, do nothing
        if currentState == newState:
            return make_response(
                jsonify(currentState),
                200
            )
        
        # update current board
        setattr(chess.state, 'fromIndex', fromIndex)
        setattr(chess.state, 'toIndex', toIndex)
        db.session.add(chess.state)

        # create and return next board position
        nextState = Move(
            pieces=newState['pieces'],
            colors=newState['colors'],
            whites_turn=newState['whites_turn'],
            fromIndex=None,
            toIndex=None,
            white_can_castle_short=newState['white_can_castle_short'],
            white_can_castle_long=newState['white_can_castle_long'],
            black_can_castle_short=newState['black_can_castle_short'],
            black_can_castle_long=newState['black_can_castle_long'],
        )
        db.session.add(nextState)
        db.session.commit()
        return make_response(
            jsonify(nextState.to_dict()),
            201
        )
    
# route to reseed database
@app.route('/seed')
def seed():
    Move.query.delete()

    starting_position = Move(
        pieces = 'RHBQKBHRPPPEEPPPEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEPPPEEPPPRHBQKBHR',
        colors = 'BBBBBBBBBBBEEBBBEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEWWWEEWWWWWWWWWWW',
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

    return make_response({}, 200)


if __name__ == '__main__':
    app.run(port=5555, debug=True)