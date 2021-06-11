from flask import Flask
from flask import request, jsonify
import controller.orders as order_service
import controller.cart as cart_service
import random
from twilio.rest import Client

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
    response = {'item': "dwd"}
    return response


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


@app.route('/orders/create', methods=['POST'])
def orders_create_order():
    resp = order_service.add_order(request.json)
    if not resp:
        return __get_error__("Error occurred", "Error occurred"), 400
    return "", 200


@app.route('/orders/all', methods=['GET'])
def orders_get_all():
    return jsonify(order_service.get_all_orders())


@app.route('/cart/create', methods=['POST'])
def create_cart():
    return jsonify(cart_service.create_cart())


@app.route('/cart', methods=['GET'])
def get_cart():
    asked_cart = cart_service.get_cart(request.args["id"])
    if not asked_cart:
        return __get_error__("Not found", "Cart not found"), 404
    return jsonify(asked_cart)


@app.route('/cart/add', methods=['PUT'])
def put_item_to_cart():
    return ""


@app.route('/sms', methods=['GET'])
def send_sms():
    account_sid = "ACc5f3165686eb763a773a6489522c6272"
    auth_token = "721622dcadda3279738362eebe634d53"
    client = Client(account_sid, auth_token)
    number = random.randint(1000, 9999)

    message = client.messages.create(
        body=str(number),
        to="+420775096687",  # Replace with your phone number
        from_="+15592010876")  # Replace with your twilio number
    return "", 200


def __get_error__(name, description):
    return {
        'error': name,
        'description': description
    }

if __name__ == '__main__':
    app.run()
