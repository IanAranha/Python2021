from flask import Flask, render_template

app = Flask(__name__)
print(__name__)


@app.route("/")
def index():
    student_info = (
       {'name' : 'Michael', 'age' : 35},
       {'name' : 'John', 'age' : 30 },
       {'name' : 'Mark', 'age' : 25},
       {'name' : 'KB', 'age' : 27}
    );
    return render_template("index.html", students = student_info, random_numbers=[2,4,7,103,55,3583])


if __name__ == "__main__":
    app.run(debug=True)