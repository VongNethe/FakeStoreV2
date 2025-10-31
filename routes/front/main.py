from flask import Flask, render_template, jsonify, request, redirect, url_for, flash
import requests
from app import app

@app.route("/")
@app.route("/home")
def home():
    product_list = []
    r = requests.get('https://fakestoreapi.com/products')
    if r.status_code == 200:
        product_list = r.json()
    return render_template('home.html', product_list=product_list)


@app.route("/product-detail")
def product_detail(pro_id):
    product = {}
    r = requests.get(f"https://fakestoreapi.com/products/{pro_id}")
    if r.status_code == 200:
        product = r.json()
    return render_template('product_detail.html', product=product)


@app.route("/cart")
def cart():
    return render_template("cart.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/api/products")
def products():
    product = [
        {
            'id': 1,
            'name': 'coca',
            'category': 'drink',
            'cost': '0.25',
            'price': '0.5',
            'image': '/static/coca.jpeg',
        }
    ]
    return jsonify(product)