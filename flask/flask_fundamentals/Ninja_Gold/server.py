from flask import Flask, redirect, render_template, request, session
import random
from datetime import datetime


app = Flask(__name__)
app.secret_key="poof"


@app.route("/")
def index():
    # session.clear()
    if "total_gold" not in session:
        session["total_gold"] = 0
        session["activity"] = []
    return render_template("index.html")

@app.route("/process_money", methods=["post"])
def process_money():
    current_time=datetime.now().strftime("%Y-%m-%d %I:%M%p")
    location = request.form["location"]
    if location == "FARM":
        random_amount=random.randrange(10,21)
        message = "<p style='color:green'>Clicked 'FARM' and earned {} gold. ({})</p>".format(random_amount, current_time)
    elif location == "CAVE":
        random_amount=random.randrange(5,11)
        message = "<p style='color:green'>Clicked 'CAVE' and earned {} gold. ({})</p>".format(random_amount, current_time)
    elif location == "HOUSE":
        random_amount=random.randrange(2,6)
        message = "<p style='color:green'>Clicked 'HOUSE' and earned {} gold. ({})</p>".format(random_amount, current_time)
    elif location == "CASINO":
        random_amount=random.randrange(-50,51)
        if random_amount > 0:
            message = "<p style='color:green'>Clicked 'CASINO' and earned {} gold. ({})</p>".format(random_amount, current_time)
        else:
            message = "<p style='color:red'>Clicked 'CASINO' and lost {} gold. ({})</p>".format(random_amount, current_time)
    session["activity"].insert(0, message)
    session["total_gold"] += random_amount
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)