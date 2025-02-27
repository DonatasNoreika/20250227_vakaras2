from flask import Flask, render_template, request, redirect
import database
app = Flask(__name__)

islaidu_zurnalas = database.nuskaityti()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/zurnalas/")
def zurnalas():
    return render_template("zurnalas.html", zurnalas=islaidu_zurnalas)

@app.route("/prideti/", methods=['GET', 'POST'])
def prideti_irasa():
    if request.method == "POST":
        suma = int(request.form['suma'])
        islaidu_zurnalas.append(suma)
        database.irasyti(suma)
        return redirect('/zurnalas/')
    return render_template("prideti.html")

@app.route("/balansas/")
def balansas():
    return render_template("balansas.html", balansas=sum(islaidu_zurnalas))

if __name__ == "__main__":
    app.run(debug=True)