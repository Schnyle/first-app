from flask import Flask, jsonify, request, make_response
from flask_migrate import Migrate
from flask_restful import Api, Resource

from models import db, Move

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)

api = Api(app)

class Moves(Resource):

    def get(self):
        return make_response(
            jsonify([m.to_dict() for m in Move.query.all()]),
            200
        )
    
api.add_resource(Moves, '/moves')

if __name__ == '__main__':
    app.run(port=5555, debug=True)