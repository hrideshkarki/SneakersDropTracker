from . import api
from flask import Flask, request, jsonify
import requests
import os
import base64
from ..models import Sneaker




@api.post('/addproducts')
def sneakerAPI():
    data = request.json
    print(data)
    shoe_name =  data[0]['shoeName']
    brand = data[0]['brand']
    silhoutte = data[0]['silhoutte']
    style_id =  data[0]['styleID']
    make = data[0]['make']
    colorway =  data[0]['colorway']
    retail_price =  data[0]['retailPrice']
    thumbnail = data[0]['thumbnail']
    release_date =  data[0]['releaseDate']
    description =  data[1]['description'] if 1 in data else data[0]['description']
    stockx =  data[0]['resellLinks']['stockX']
    fightclub = data[0]['resellLinks'].get('flightClub', 1)
    goat =  data[0]['resellLinks'].get('goat', 1)

    sneaker = Sneaker.query.filter_by(shoe_name = shoe_name).first()

    if sneaker:
        return {
            'status': 'not ok',
            'message': 'This sneaker has already been added.'
        }, 400

    sneaker = Sneaker(shoe_name, brand, silhoutte, style_id, make, colorway, retail_price, thumbnail, release_date, description, stockx, fightclub, goat) 
    sneaker.save_to_db()
    return {
        'status': 'ok',
        'message': "You have successfully added sneaker to your database."
    }, 201


    
