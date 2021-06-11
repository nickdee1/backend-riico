from flask import Flask
from flask import request, jsonify
import pymongo

app = Flask(__name__)

# client = pymongo.MongoClient("mongodb+srv://riico_user:riico123@riicocluster.lovtu.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
# db = client.test
#
# mycol = db["furniture"]


@app.route('/')
def hello_world():
	response = {'item': "dwd"}
	return response


if __name__ == '__main__':
	app.run()
