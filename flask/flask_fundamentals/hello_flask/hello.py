from flask import Flask, render_template            ##Import Flask

app = Flask(__name__)                               ##Global variable __name__ tells Flask we are importing it.

print(__name__)                                     ##Just for fun


@app.route("/")                     ##This is run when we do localhost5000:
def Hello_World():
    # return "HELLO WORLD!!!"
    return render_template("index.html", name="Ian")

@app.route("/success")
def Success():
    return "S U C C E S S"

@app.route("/hello/<name>")
def Hello(name):
    print(name)
    return "Hello "+name

@app.route("/users/<username>/<id>")
def show_user_id(username, id):
    print(username)
    print(id)
    return "<p>Username: " + username + "</p><p>ID: " + id +"</p>"




if __name__ == "__main__":
    app.run(debug=True)
