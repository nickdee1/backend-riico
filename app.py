from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)

client = PyMongo.MongoClient("mongodb+srv://riico_user:riico123@riicocluster.lovtu.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.test


@app.route('/')
def hello_world():

	return 'Hello World!'


if __name__ == '__main__':
	app.run()
