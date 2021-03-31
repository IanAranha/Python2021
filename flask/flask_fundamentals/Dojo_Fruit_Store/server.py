from flask import Flask, render_template, redirect, request
from datetime import datetime
import calendar

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/checkout", methods=["post"])
def checkout():
    count=0
    count_strawberry = int(request.form["qty_Strawberry"])
    count_raspberry = int(request.form["qty_Raspberry"])
    count_apple = int(request.form["qty_Apple"])
    count  = count + count_strawberry + count_raspberry + count_apple
    x = datetime.today().strftime("%B %d, %Y at %I:%M %p")
    return render_template("checkout.html", counts = count, x = x)

@app.route("/goBack", methods=["post"])
def goBack():
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)