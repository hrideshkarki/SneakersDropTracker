from . import api
from flask import Flask, jsonify
from ..models import Sneaker 

@api.get('/sneakers')
def get_sneakers():
    sneakers = Sneaker.query.all()  # Retrieve all sneaker objects from the database

    # Serialize sneaker data into JSON format
    serialized_sneakers = []
    for sneaker in sneakers:
        serialized_sneakers.append({
            'shoe_name': sneaker.shoe_name,
            'brand': sneaker.brand,
            'silhoutte': sneaker.silhoutte,
            'style_id': sneaker.style_id,
            'make': sneaker.make,
            'colorway': sneaker.colorway,
            'retial_price': sneaker.retial_price,
            'thumbnail': sneaker.thumbnail,
            'release_date': sneaker.release_date,
            'description': sneaker.description,
            'stockx': sneaker.stockx,
            'fightclub': sneaker.fightclub,
            'goat': sneaker.goat
        })

    return jsonify({'sneakers': serialized_sneakers})