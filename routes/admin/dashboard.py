from sys import modules

from flask import Flask, render_template
import requests
from app import app

@app.get("/admin")
@app.get("/admin/dashboard")
def dashboard():
    return render_template('admin/dashboard/index.html', modules='dashboard')