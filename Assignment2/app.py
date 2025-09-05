from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    list_of_names = []
    with open("books.txt", "r", encoding="UTF-8")as f:
        for line in f:
            line = line.strip()
            if(line):
              list_of_names.append(line)
    if len(list_of_names) == 0:
      return render_template("index.html", message = "No books in the library yet.")
    return render_template("index.html", names = list_of_names)  

@app.route("/add", methods = ["GET", "POST"])
def add():
    if request.method == "GET":
       return render_template("add.html")
    else:
        title = request.form.get('title', 'NaN')
        author = request.form.get('author', 'NaN')
        with open("books.txt", "a", encoding="UTF-8") as f:
           f.write(f"{title} - {author}\n")
        return render_template("add.html", message = "Book Added successfully! ✅")   
           

app.run(debug=True)    

