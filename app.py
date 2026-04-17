from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def reverse():

    if request.method == "POST":

        text = request.form["text"]

        result = text[::-1]

        return f"Teskari matn: {result}"

    return render_template("index.html")

app.run(debug=True)
