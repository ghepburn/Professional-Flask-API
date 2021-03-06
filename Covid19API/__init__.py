from flask import Flask, session
# from flask.ext.session import Session
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
import requests
import datetime as dt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '0ff50a478fde6e0ee2f3eeaf66657a84'
app.config['REMEMBER_COOKIE_DURATION'] = dt.timedelta(seconds=10000)


db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from . import routes