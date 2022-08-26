"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Character, Planet, Vehicle, Starship, Favorite
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code


# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)


# Users
@app.route('/users', methods=['GET'])
@app.route('/users/<int:user_id>', methods=['GET'])
def handle_users(user_id=None):
    if user_id is None:
        users = User.query.all()
        users = [x.serialize() for x in users]
        return jsonify(users), 200
    
    user = User.query.filter_by(id=user_id).first()
    if user is not None:
        return jsonify(user.serialize()), 200

    return jsonify({"msg": "Request not valid"}), 400


# Characters
@app.route('/characters', methods=['GET'])
@app.route('/characters/<int:character_id>', methods=['GET'])
def handle_characters(character_id=None):
    if character_id is None:
        characters = Character.query.all()
        characters = [x.serialize() for x in characters]
        return jsonify(characters), 200
    
    character = Character.query.filter_by(id=character_id).first()
    if character is not None:
        return jsonify(character.serialize()), 200

    return jsonify({"msg": "Request not valid"}), 400


# Planets
@app.route('/planets', methods=['GET'])
@app.route('/planets/<int:planet_id>', methods=['GET'])
def handle_planets(planet_id=None):
    if planet_id is None:
        planets = Planet.query.all()
        planets = [x.serialize() for x in planets]
        return jsonify(planets), 200
    
    planet = Planet.query.filter_by(id=planet_id).first()
    if planet is not None:
        return jsonify(planet.serialize()), 200

    return jsonify({"msg": "Request not valid"}), 400


# Vehicles
@app.route('/vehicles', methods=['GET'])
@app.route('/vehicles/<int:vehicle_id>', methods=['GET'])
def handle_vehicles(vehicle_id=None):
    if vehicle_id is None:
        vehicles = Vehicle.query.all()
        vehicles = [x.serialize() for x in vehicles]
        return jsonify(vehicles), 200
    
    vehicle = Vehicle.query.filter_by(id=vehicle_id).first()
    if vehicle is not None:
        return jsonify(vehicle.serialize()), 200

    return jsonify({"msg": "Request not valid"}), 400


# Starships
@app.route('/starships', methods=['GET'])
@app.route('/starships/<int:starship_id>', methods=['GET'])
def handle_starships(starship_id=None):
    if starship_id is None:
        starships = Starship.query.all()
        starships = [x.serialize() for x in starships]
        return jsonify(starships), 200
    
    starship = Starship.query.filter_by(id=starship_id).first()
    if starship is not None:
        return jsonify(starship.serialize()), 200

    return jsonify({"msg": "Request not valid"}), 400
    

# Favorites
@app.route('/favorites', methods=['GET'])
@app.route('/favorites/<int:favorite_id>', methods=['GET'])
def handle_favorites(favorite_id=None):
    if favorite_id is None:
        favorites = Favorite.query.all()
        favorites = [x.serialize() for x in favorites]
        return jsonify(favorites), 200
    
    favorite = Favorite.query.filter_by(id=favorite_id).first()
    if favorite is not None:
        return jsonify(favorite.serialize()), 200

    return jsonify({"msg": "Request not valid"}), 400


# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
