from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/<x>/<y>")
def index2(x, y):
    y = int(y)
    y2 = int(y/2)
    x = int(x)
    x2 = int(x/2)
    return render_template("index2.html", xForward = x2, yForward = y2)

if __name__ == "__main__":
    app.run(debug=True)