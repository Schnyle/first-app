from flask import Flask, jsonify, request, make_response
from flask_migrate import Migrate
from flask_restful import Api, Resource
from flask_cors import CORS

from models import db, Move

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
        this_move = Move.query.order_by(Move.id.desc()).first()
        data = request.get_json()
        for key in data:
            setattr(this_move, key, data[key])
        db.session.add(this_move)
        db.session.commit()
        response = make_response(
            jsonify(this_move.to_dict()),
            200
        )
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

if __name__ == '__main__':
    app.run(port=5555, debug=True)