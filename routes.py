#!/usr/bin/python3
# -*- coding: utf-8 -*-

import logging

from flask import request, redirect, render_template, session, url_for, jsonify
from utils import app, api, cursor, conn


@app.route("/session", methods=['GET'])
def session_view():
	return jsonify({"country_code": session["country_code"],
		"phone_number": session["phone_number"]})


@app.route("/phone_verification", methods=["GET", "POST"])
def phone_verification():
	if request.method == "POST":
		data = request.get_json()
		if data:
			country_code = data["country_code"]
			phone_number = data["phone_number"]
		elif request.form.get("country_code") and request.form.get("phone_number"):
			country_code = request.form.get("country_code")
			phone_number = request.form.get("phone_number")
		else:
			return jsonify({"message": "bad request body"})

		session["country_code"] = country_code
		session["phone_number"] = phone_number

		api.phones.verification_start(phone_number, country_code, via="sms")
		return redirect(url_for("verify"))

	return render_template("phone_verify.html")


@app.route("/verify", methods=["GET", "POST"])
def verify():
	if request.method == "POST":
		data = request.get_json()
		if data:
			token = data["token"]
		elif request.form.get("token"):
			token = request.form.get("token")
		else:
			return jsonify({"message": "bad request body"})

		phone_number = session.get("phone_number")
		country_code = session.get("country_code")

		verification = api.phones.verification_check(phone_number, country_code, token)

		if verification.ok():
			return jsonify(verification.ok())

	return render_template("verify.html")


@app.route("/furnitures/<furniture_id>", methods=['GET'])
def detail_furniture(furniture_id):
	"""detail of a furniture"""

	cursor.execute(f"SELECT * FROM component WHERE furniture_id = {furniture_id}")
	components = cursor.fetchall()
	data = []
	for component in components:
		data.append({ \
			'id': component[0],
			'name': component[2],
			'price': component[3]})

	cursor.execute(f"SELECT * FROM furniture WHERE id = {furniture_id}")
	furniture = cursor.fetchone()
	if not furniture:
		response = {'message': 'furniture does not exist'}
		return jsonify(response), 404
	furniture_data = { \
			'id': furniture[0],
			'category': furniture[1],
			'name': furniture[2],
			'color': furniture[3],
			'location': furniture[4],
			'material': furniture[5],
			'width': furniture[6],
			'height': furniture[7],
			'components': data}

	ret = jsonify(furniture_data)

	logging.info('detail_furniture(furniture_id=%s) -> ret=%s', (furniture_id, ret))
	return ret


@app.route("/furnitures", methods=["GET"])
def search_furniture():
	"""all furnitures"""

	cursor.execute("SELECT * FROM furniture")
	furnitures = cursor.fetchall()
	data = []
	for furniture in furnitures:
		data.append({ \
			'id': furniture[0],
			'category': furniture[1],
			'name': furniture[2],
			'color': furniture[3],
			'location': furniture[4],
			'material': furniture[5],
			'width': furniture[6],
			'height': furniture[7]})
	ret = jsonify({"furnitures": data})

	logging.info('search_furniture() -> ret=%s', ret)
	return ret


@app.route("/cart/create", methods=["POST"])
def create_cart():
	cursor.execute("insert into cart (total_price) values (0.0) returning id")
	cart_id = cursor.fetchone()
	conn.commit()
	return jsonify({"id": cart_id[0]})

@app.route("/cart/cart_item_decrease/<cart_item_id>", methods=["GET", "POST"])
def decrease_cart_item_count(cart_item_id):
	pass

@app.route("/cart_item_increase/<cart_item_id>", methods=["GET", "POST"])
def increase_cart_item_count(cart_item_id):
	cursor.execute(f"SELECT * FROM cart WHERE id={cart_item_id}")
	cart = cursor.fetchall()
	if not cart:
		response = {'message': 'cart does not exist'}
		return jsonify(response), 404


@app.route("/cart/<cart_id>/add/<component_id>", methods=["PUT"])
def put_to_cart(cart_id, component_id):
	cursor.execute(f"SELECT * FROM cart WHERE id={cart_id}")
	cart = cursor.fetchall()
	if not cart:
		response = {'message': 'cart does not exist'}
		return jsonify(response), 404
	gotten_cart = cart[0]
	cursor.execute(f"SELECT * FROM component WHERE id={component_id}")
	component = cursor.fetchall()
	if not component:
		response = {'message': 'component does not exist'}
		return jsonify(response), 404
	gotten_component = component[0]
	cursor.execute(f"SELECT * FROM cart_item WHERE cart_id={cart_id} AND item_id={component_id}")
	existing_cart_items = cursor.fetchall()
	if not existing_cart_items:
		cursor.execute(f"insert into cart_item (price, cart_id, item_id) values ({gotten_component[1]}, {gotten_cart[0]}, {gotten_component[0]})")
		cursor.execute(f"update cart set total_price = {gotten_cart[1] + gotten_component[1]}")
		conn.commit()
		return redirect(url_for('increase_cart_item_count'))
	else:
		return redirect(url_for('decrease_cart_item_count'))
		print("")
	return ""



@app.route("/components/<component_id>", methods=['GET'])
def detail_component(component_id):
	"""detail of a component"""

	cursor.execute(f"SELECT * FROM component WHERE id = {component_id}")
	component = cursor.fetchone()
	if not component:
		response = {'message': 'component does not exist'}
		return jsonify(response), 404
	result = {\
		'id': component[0],
		'name': component[1],
		'price': component[2]}
	ret = jsonify(result)

	logging.info('detail_component(component_id=%s) -> ret=%s', (component_id, ret))
	return ret


@app.route("/components", methods=["GET"])
def search_components():
	"""all components"""

	cursor.execute("SELECT * FROM component")
	components = cursor.fetchall()

	dicts = []
	for component in components:
		dicts.append({ \
			'id': component[0],
			'name': component[1],
			'price': component[2]})
	ret = jsonify({"components": dicts})

	logging.info('search_components() -> ret=%s', ret)
	return ret

