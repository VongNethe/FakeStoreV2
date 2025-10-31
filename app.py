from flask import Flask, render_template, jsonify, request, redirect, url_for, flash
import requests
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db=SQLAlchemy(app)
migrate = Migrate(app, db)

import models

import routes


