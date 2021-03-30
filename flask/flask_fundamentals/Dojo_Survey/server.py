from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/users", methods={"POST"})
def results():
    return render_template("result.html")

@app.route("/back", methods=["post"])
def back():
    return redirect("/")

@app.route("/danger")
def danger():
    print('A user tried to visit /danger.  We have redirected the user to /')
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)