from flask import Flask, render_template, redirect, request, session, flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)
app.secret_key="005ThisIsASecret"


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process", methods=["post"])
def process():
    if len(request.form["email"]) < 1:
        flash("Email cannot be empty", "email")
    elif not EMAIL_REGEX.match(request.form["email"]):
        flash("Invalid email", "email")
    # else:
    #     flash("Hello! You entered a valid email")
    
    if '_flashes' in session.keys():
        return redirect("/")
    else:
        return redirect("/success")


@app.route("/success")
def success():
    return render_template("success.html")


@app.route("/back_to_home", methods=["post"])
def back_to_home():
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)

