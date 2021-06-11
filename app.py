from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)

components = [
	{
		'name': 'screw',
		'price': 25
	},
	{
		'name': 'nut',
		'price': 14
	}
]

all_furniture = [
	{
		'id': 1,
		'name': 'chair',
		'color': 'blue',
		'components': components
	},
	{
		'id': 2,
		'name': 'chair',
		'color': 'blue',
		'components': components
	}
]

cart = {
	'items': components
}

orders = [{
	'id': 1,
	'items': components,
	'total_price': 39,
	'state': 'finished'
}]


@app.route('/')
def hello_world():
	return 'Hello World!'


@app.route('/furniture/all')
def furniture_get_all():
	return jsonify(all_furniture)


@app.route('/furniture')
def furniture_get_item():
	request_id = request.args["id"]
	for el in all_furniture:
		if el["id"] == int(request_id):
			return el

	return __get_error__("Not found", "Furniture not found"), 404


@app.route('/orders')
def orders_get_order():
	request_id = request.args["id"]
	for el in orders:
		if el['id'] == int(request_id):
			return el

	return __get_error__("Not found", "order not found"), 404


def __get_error__(name, description):
	return {
		'error': name,
		'description': description
	}


if __name__ == '__main__':
	app.run()
