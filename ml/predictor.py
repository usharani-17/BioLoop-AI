import pandas as pd
import joblib

# Load trained model
model = joblib.load("ml/Model/cbg_model.pkl")


def predict_output(waste_type, quantity, location):
    # Create input data
    input_data = pd.DataFrame({
        "Waste_Type": [waste_type],
        "Quantity_kg": [quantity],
        "Location": [location]
    })

    # Make prediction
    prediction = model.predict(input_data)

    cbg = round(prediction[0][0], 2)
    revenue = round(prediction[0][1], 2)
    slurry = round(prediction[0][2], 2)

    return cbg, revenue, slurry
if __name__ == "__main__":
    cbg, revenue, slurry = predict_output(
        "Food Waste",
        5000,
        "Chennai"
    )

    print("CBG Yield:", cbg)
    print("Revenue:", revenue)
    print("Slurry:", slurry)