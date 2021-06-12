#!/usr/bin/python3
# -*- coding: utf-8 -*-


import os

from utils import conn, cursor, app
from routes import *


<<<<<<< HEAD
=======
with open(os.path.join("db", "create.sql")) as f:
	cursor.executescript(f.read())
	conn.commit()
>>>>>>> 971b489c707d9ad6b0651f431ee3d68cd13a31cf

if __name__ == '__main__':
	app.run(debug=True, host="0.0.0.0")
