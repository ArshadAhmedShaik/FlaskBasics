from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    marks = {
    "harry": 56,
    "Rohan": 67,
    "Aakash": 78,
    "Shubham": 100,
    "Reena": 67
     }
    values = [1, marks, 67]
    # we can jsonify a list
    return jsonify(values)

app.run(debug=True)