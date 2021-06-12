#!/usr/bin/python3
# -*- coding: utf-8 -*-


import os

from utils import conn, cursor, app
from routes import *


with open(os.path.join("db", "create.sql")) as f:
	cursor.executescript(f.read())
	conn.commit()


if __name__ == '__main__':
	app.run(debug=True, host="0.0.0.0")
