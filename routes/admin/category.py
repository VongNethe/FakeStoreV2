from sys import modules

from flask import Flask, render_template
import requests
from app import app

@app.get("/admin/category")
def category_index():
    return render_template('admin/category/index.html', modules='category')

@app.get("/admin/category/list")
def category_list():
    categories =get_category_list()
    return  categories

@app.post("/admin/create")
def create():
    return "Create Category"

def get_category_list():
    return [
        {'id':1, 'name': 'Electronics'},
        {'id': 2, 'name': 'Books'},
        {'id': 3, 'name': 'Clothing'},
        {'id': 4, 'name': 'Home & Kitchen'},
        {'id': 5, 'name': 'Sports & Outdoors'},
    ]
