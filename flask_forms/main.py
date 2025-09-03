from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def hello_world():
    if request.method == "POST":
        with open("file.txt", "w") as f:
            f.write(f"Name is {request.form.get("Name", "NAN")} and email is {request.form.get("Email", "NAN")}")
        return f"Submitted the form successfully"    
    return render_template("contact.html")

app.run(debug=True)