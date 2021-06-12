#!/usr/bin/python3
# -*- coding: utf-8 -*-


import sqlite3
from flask import Flask
from authy.api import AuthyApiClient
from flask_session import Session
from flask_marshmallow import Marshmallow
from flask_cors import CORS

from config import Config


app = Flask(__name__)
app.config.from_object(Config)

api = AuthyApiClient(app.config['AUTHY_API_KEY'])
conn = sqlite3.connect('db/riico.db', check_same_thread=False)
cursor = conn.cursor()

ma = Marshmallow(app)
cors = CORS(app)
sess = Session()
sess.init_app(app)
