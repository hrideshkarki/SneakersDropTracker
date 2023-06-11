from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import UserMixin
# import requests
from werkzeug.security import generate_password_hash
from secrets import token_hex

db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(45), nullable = False)
    last_name = db.Column(db.String(45), nullable = False)
    username = db.Column(db.String(45), nullable = False, unique = True)
    email = db.Column(db.String(100), nullable = False, unique = True)
    password = db.Column(db.String, nullable = False)
    date_created = db.Column(db.DateTime, nullable = False, default=datetime.utcnow())
    is_admin = db.Column(db.Boolean, default=False)
    api_token = db.Column(db.String, unique=True)
    sneakers = db.relationship('Sneaker', secondary = 'fav', backref='fav_owner', lazy=True)

    def __init__(self, first_name, last_name, username, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.password = generate_password_hash(password),
        self.api_token = token_hex(16)

    def add_to_fav(self, product):
        self.products.append(product) 
        db.session.commit()

    def remove_from_fav(self, product):
        self.products.remove(product) 
        db.session.commit()

    def empty_fav(self):
        self.products.clear() 
        db.session.commit()
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def save_changes(self):
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def to_dict(self):
        return {
            "id" : self.id, 
            "first_name": self.first_name,
            "last_name" : self.last_name,
            "username" : self.username,
            "email" : self.email,
            "api_token" : self.api_token,
        }


class Sneaker(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    shoe_name = db.Column(db.String(300), unique = True, nullable = False)
    brand = db.Column(db.String(100), nullable = False)
    silhoutte = db.Column(db.String(100), nullable = False)
    style_id = db.Column(db.String(100), nullable = False)
    make = db.Column(db.String(100), nullable = False)
    colorway = db.Column(db.String(100), nullable = False)
    retial_price = db.Column(db.Float, nullable = False)
    thumbnail = db.Column(db.String, nullable = False, unique = True)
    release_date = db.Column(db.String(30), nullable = False)
    description = db.Column(db.String, nullable = False)
    stockx = db.Column(db.String, nullable = False)
    fightclub = db.Column(db.String, nullable = False)
    goat = db.Column(db.String, nullable = False)
    date_created = db.Column(db.DateTime, nullable = False, default=datetime.utcnow())
    in_fav = db.relationship("User", secondary = "fav", overlaps="fav_owner,sneakers")


    
    def __init__(self, shoe_name, brand, silhoutte, style_id, make, colorway, retial_price, thumbnail, release_date, description, stockx, fightclub, goat):
        self.shoe_name = shoe_name
        self.brand = brand
        self.silhoutte = silhoutte
        self.style_id = style_id
        self.make = make
        self.colorway = colorway
        self.retial_price = retial_price
        self.thumbnail = thumbnail
        self.release_date = release_date
        self.description = description
        self.stockx = stockx
        self.fightclub = fightclub
        self.goat = goat
        self.retial_price = retial_price

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def save_changes(self):
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

fav = db.Table('fav',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('sneaker_id', db.Integer, db.ForeignKey('sneaker.id'), primary_key=True)
)
