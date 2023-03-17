import sys
sys.path.insert(0, './chess')

from flask import Flask, jsonify, request, make_response
from flask_migrate import Migrate
from flask_restful import Api, Resource
from flask_cors import CORS

from models import db, Move
import chess

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)

api = Api(app)

with app.app_context():
    initial_state = Move.query.order_by(Move.id.desc()).first()
    chess = chess.Chess(initial_state)

# print(chess.state.to_dict())

@app.route('/moves', methods=['GET', 'PATCH'])
def moves():

    if request.method == 'GET':
        return make_response(
            jsonify([m.to_dict() for m in Move.query.all()]),
            200
        )
    
    if request.method == 'PATCH':
        data = request.get_json()
        fromIndex = data['fromIndex']
        toIndex = data['toIndex']
        # check if valid move
        currentState = chess.state_dict.copy()
        newState = chess.move(fromIndex, toIndex)
        print('app.py newState:', newState)
        print('app.py currentState:', currentState)
        # if invalid move, do nothing
        if currentState == newState:
            print('app.py: did not update game state')
            currentState['fromIndex'] = fromIndex
            currentState['toIndex'] = toIndex
            return make_response(
                jsonify(currentState),
                200
            )
        # update current board
        setattr(chess.state, 'fromIndex', fromIndex)
        setattr(chess.state, 'toIndex', toIndex)
        db.session.add(chess.state)
        # create next board position
        nextState = Move(
            pieces=newState['pieces'],
            colors=newState['colors'],
            whites_turn=newState['whites_turn'],
            fromIndex=None,
            toIndex=None
        )
        db.session.add(nextState)
        db.session.commit()
        print('app.py: updated game state')
        print(nextState)
        return make_response(
            jsonify(nextState.to_dict()),
            201
        )

if __name__ == '__main__':
    app.run(port=5555, debug=True)