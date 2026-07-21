from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    brand = request.form["brand"]
    year = request.form["model_year"]
    km = request.form["km_driven"]

    return f"""
    Brand : {brand}<br>
    Model Year : {year}<br>
    KM Driven : {km}
    """


if __name__ == "__main__":
    app.run(debug=True)