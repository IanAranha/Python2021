from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)
app.secret_key = "0003ThisIsASecretKey"

@app.route("/")
def index():
    session["counter"] = 0
    return redirect("/add")

@app.route("/destroy_session")
def destroy_session():
    session.clear()
    return redirect("/")

@app.route("/add")
def add():
    session["counter"]+=1
    return render_template("index.html")

@app.route("/add2", methods=["post"])
def add2():
    session["counter"] += 2
    return render_template("index.html")

@app.route("/reset", methods=["post"])
def reset():
    return redirect("/destroy_session")




if __name__ == "__main__":
    app.run(debug=True)