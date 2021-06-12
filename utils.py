#!/usr/bin/python3
# -*- coding: utf-8 -*-


import sqlite3
from flask import Flask
from authy.api import AuthyApiClient
from flask_session import Session
from flask_marshmallow import Marshmallow
from flask_cors import CORS
import psycopg2

from config import Config


app = Flask(__name__)
app.config.from_object(Config)

api = AuthyApiClient(app.config['AUTHY_API_KEY'])
db_url = "postgres://brdkqnvctnlapx:8a09de01512251687a8d62354cb20bce6c18c70c9a98af0f340535b7af77c9f9@ec2-108-128-104-50.eu-west-1.compute.amazonaws.com:5432/d2hpaqjvlo7kn0"
conn = psycopg2.connect(db_url, sslmode='require')
cursor = conn.cursor()

ma = Marshmallow(app)
cors = CORS(app)
sess = Session()
sess.init_app(app)
