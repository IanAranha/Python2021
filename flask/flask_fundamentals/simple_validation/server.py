from flask import Flask, render_template, redirect, request, session, flash


app = Flask(__name__)
app.secret_key="005ThisIsASecret"


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process", methods=["post"])
def process():
    if len(request.form["name"]) < 1:
        print(len(request.form["name"]))
        print("Name cannot be empty")
        flash("Name cannot be empty")
    else:
        print(len(request.form["name"]))
        print("Hello {}".format(request.form["name"]))
        flash("Hello {}".format(request.form["name"]))
    return redirect("/")



if __name__ == "__main__":
    app.run(debug=True)