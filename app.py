from flask import Flask
import pymongo

app = Flask(__name__)

client = pymongo.MongoClient("mongodb+srv://riico_user:riico123@riicocluster.lovtu.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.test


@app.route('/')
def hello_world():
	# test_data = db.
	return 'Hello World!'


if __name__ == '__main__':
	app.run()
