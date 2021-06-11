from flask import jsonify
import controller.orders as order_service

from app import app


@app.route('/orders/all', methods=['GET'])
def orders_get_all():
    return jsonify(order_service.get_all_orders())
