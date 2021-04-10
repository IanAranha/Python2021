from flask import Flask, redirect, render_template, session, request
import random

app = Flask(__name__)
app.secret_key = "0004ThisIsASecretKey"


@app.route("/")
def index():
	if "random_number" not in session:
	 	session["random_number"] = random.randrange(0, 101)
	return render_template("index.html")


@app.route("/guess", methods=["post"])
def guess():
	if request.form["input"] == "":
		print("Cannot be blank")
		return redirect("/")
	session["guessed_num"] = int(request.form["input"])
	if session["guessed_num"] < session["random_number"]:
		session["state"] = "low"
	elif session["guessed_num"] > session["random_number"]:
		session["state"] = "high"
	else:
		session["state"] = "correct"
	return redirect("/")

@app.route("/reset", methods=["post"])
def reset():
	session.clear()
	return redirect('/')


if __name__ == "__main__":
	app.run(debug=True)
