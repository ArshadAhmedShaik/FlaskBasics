from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    marks = {
        "John": 45,
        "Saurav":89,
        "Mark":34,
        "Jeff":65,
        "Alexa":90,
        "Lilly":100
    }
    # how to pass marks variable into this template
    return render_template("index.html", marks = marks)

app.run(debug=True)