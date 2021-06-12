#!/usr/bin/python3
# -*- coding: utf-8 -*-

import logging

from flask import request, redirect, render_template, session, url_for, jsonify
from utils import app, api, cursor


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

