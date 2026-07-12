import os
from flask import Flask, render_template, request
from ml.predictor import predict_output

app = Flask(__name__)

# -----------------------------
# Location Coordinates
# -----------------------------
locations = {
    "Chennai": (13.0827, 80.2707),
    "Coimbatore": (11.0168, 76.9558),
    "Madurai": (9.9252, 78.1198),
    "Salem": (11.6643, 78.1460),
    "Trichy": (10.7905, 78.7047)
}


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    # User Inputs
    waste_type = request.form["waste_type"]
    quantity = float(request.form["quantity"])
    location = request.form["location"]

    # ML Prediction
    cbg, revenue, slurry = predict_output(
        waste_type,
        quantity,
        location
    )

    # -----------------------------
    # AI Recommendation
    # -----------------------------

    if waste_type == "Food Waste":

        recommendation = """
Food Waste has a high methane generation potential.

✔ Recommended Method:
Anaerobic Digestion

✔ Final Product:
Compressed Biogas (CBG)

✔ By-product:
Organic Slurry

✔ Suitable Users:
Farmers, Municipal Corporations and Biogas Plants.
"""

    elif waste_type == "Cow Dung":

        recommendation = """
Cow Dung is one of the best raw materials for biogas production.

✔ Produces high-quality CBG.

✔ Generates organic fertilizer.

✔ Highly suitable for rural biogas plants.
"""

    elif waste_type == "Poultry Waste":

        recommendation = """
Poultry Waste contains high organic matter.

✔ Recommended Method:
Controlled Anaerobic Digestion

✔ Suitable for Commercial Biogas Plants.

✔ High methane generation potential.
"""

    elif waste_type == "Vegetable Waste":

        recommendation = """
Vegetable Waste decomposes rapidly.

✔ Best suited for small-scale biogas plants.

✔ Produces nutrient-rich slurry.
"""

    elif waste_type == "Fruit Waste":

        recommendation = """
Fruit Waste has high moisture and sugar content.

✔ Produces quality biogas.

✔ Generates organic fertilizer.
"""

    else:

        recommendation = """
Agricultural Residue can be converted into renewable energy.

✔ Recommended Method:
Biogas Digestion

✔ Can also be converted into Bio-CNG.
"""

    # -----------------------------
    # Environmental Calculations
    # -----------------------------

    co2_saved = round(cbg * 2.3, 2)

    landfill_saved = round(quantity, 2)

    electricity = round(cbg * 1.8, 2)

    sustainability = min(
        100,
        round((cbg / quantity) * 1000, 1)
    )

    # -----------------------------
    # Map Coordinates
    # -----------------------------

    latitude, longitude = locations.get(
        location,
        (13.0827, 80.2707)
    )

    # -----------------------------
    # Render Result Page
    # -----------------------------

    return render_template(

        "result.html",

        waste_type=waste_type,

        quantity=quantity,

        location=location,

        cbg=cbg,

        revenue=revenue,

        slurry=slurry,

        co2_saved=co2_saved,

        landfill_saved=landfill_saved,

        electricity=electricity,

        sustainability=sustainability,

        latitude=latitude,

        longitude=longitude,

        recommendation=recommendation

    )


import os

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        debug=True
    )