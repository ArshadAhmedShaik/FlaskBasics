from flask import Flask, render_template, request

app = Flask(__name__, static_folder="assets", static_url_path="/public")

@app.route("/")
def home():
    users = []
    with open("in.txt", "r") as f:
       for line in f:
           line = line.strip()
           if line:
               users.append(line)
    return render_template("index.html", users = users)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "GET":
        return render_template("contact.html")
    elif request.method == "POST":
         name = request.form.get("name")
         email = request.form.get("email")
         if not name or not email:
             return render_template("contact.html", message="⚠ Please fill all fields")
         else:    
          with open("data.txt", "a") as f:
              f.write(f"{name} - {email}\n")
          return render_template("contact.html", message = f"Thank You, {name}!")
    return render_template("contact.html")

app.run(debug=True)