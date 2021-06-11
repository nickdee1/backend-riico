from flask import Flask

from flask import request, redirect, render_template, session, url_for, jsonify

from utils import app, api, cursor


app = Flask(__name__)
app.config["DEBUG"] = True


# @app.route("/session", methods=['GET'])
# def session_view():
#     return jsonify({"country_code": session["country_code"],
#                     "phone_number": session["phone_number"]})


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
def get_furniture(furniture_id):
	cursor.execute(f"SELECT * FROM furniture WHERE id = {furniture_id}")
	furniture = cursor.fetchone()
	if not furniture:
		response = {\
			'message': 'furniture does not exist'}
		return jsonify(response), 404
	result = {\
		'id': furniture[0],
		'component_id': furniture[1],
		'category': furniture[2],
		'name': furniture[3],
		'color': furniture[4],
		'location': furniture[5],
		'material': furniture[6],
		'width': furniture[7],
		'height': furniture[8]}
	return jsonify(result)


@app.route("/furnitures", methods=["GET"])
def course_list():
	cursor.execute("SELECT * FROM furniture")
	furnitures = cursor.fetchall()

	dicts = []
	for furniture in furnitures:
		dicts.append({ \
			'id': furniture[0],
			'component_id': furniture[1],
			'category': furniture[2],
			'name': furniture[3],
			'color': furniture[4],
			'location': furniture[5],
			'material': furniture[6],
			'width': furniture[7],
			'height': furniture[8]})

	return jsonify({
		"furnitures": dicts})


if __name__ == '__main__':
	app.run()
