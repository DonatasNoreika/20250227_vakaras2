from flask import Flask, render_template

app = Flask(__name__)

islaidu_zurnalas = [700, -20, -30]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/zurnalas/")
def zurnalas():
    return render_template("zurnalas.html", zurnalas=islaidu_zurnalas)

if __name__ == "__main__":
    app.run(debug=True)