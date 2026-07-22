from flask import Flask, render_template, request,jsonify
import joblib
import pandas as pd
app = Flask(__name__)
model = joblib.load("../models/deployment_model.joblib")
df = pd.read_csv("../data/processed/cleaned_used_cars.csv")

brands = sorted(df["brand"].dropna().unique())
fuel_types = sorted(df["fuel_type"].dropna().unique())
transmissions = sorted(df["transmission"].dropna().unique())
body_types = sorted(df["body_type"].dropna().unique())
cities = sorted(df["city_x"].dropna().unique())
owners = sorted(df["owner_type"].dropna().unique())


@app.route("/")
def home():
    return render_template(
        
        "index.html",
        brands=brands,
        fuel_types=fuel_types,
        transmissions=transmissions,
        body_types=body_types,
        cities=cities,
        owners=owners
    )


@app.route("/predict", methods=["POST"])
def predict():

    brand = request.form["brand"]
    model_name = request.form["model"]
    model_year = int(request.form["model_year"])
    fuel_type = request.form["fuel_type"]
    transmission = request.form["transmission"]
    body_type = request.form["body_type"]
    city = request.form["city_x"]
    owner = request.form["owner_type"]
    km_driven = float(request.form["km_driven"])

    input_data = pd.DataFrame({
        "brand": [brand],
        "model": [model_name],
        "model_year": [model_year],
        "fuel_type": [fuel_type],
        "transmission": [transmission],
        "body_type": [body_type],
        "city_x": [city],
        "owner_type": [owner],
        "km_driven": [km_driven]
    })

    prediction = model.predict(input_data)

    predicted_price = round(prediction[0], 2)

    return jsonify({

    "predicted_price": f"{predicted_price:,.2f}",

    "brand": brand,

    "model": model_name,

    "year": model_year,

    "fuel": fuel_type,

    "transmission": transmission,

    "body": body_type,

    "city": city,

    "owner": owner,

    "km": km_driven

})


@app.route("/get_models/<brand>")
def get_models(brand):

    models = sorted(
        df[df["brand"] == brand]["model"]
        .dropna()
        .unique()
        .tolist()
    )

    return jsonify(models)


if __name__ == "__main__":
    app.run(debug=True)

