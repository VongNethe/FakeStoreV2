from email.policy import default

from app import db

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    cost = db.Column(db.Numeric(10,2))
    price = db.Column(db.Numeric(10,2))
    category = db.Column(db.Integer)
    image = db.Column(db.String(128),nullable=True)
    stock = db.Column(db.Integer, default=0)