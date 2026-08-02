
# Import necessary libraries
import joblib
import pandas as pd
from flask import Flask, request, jsonify

# Initialize Flask application
superkart_sales_api = Flask("SuperKart Sales Prediction API")

# Load trained model
model = joblib.load("prediction_model_v1.joblib")

# ----------------------------------------------------
# Home Route
# ----------------------------------------------------
@superkart_sales_api.get("/")
def home():
    return "Welcome to the SuperKart Sales Prediction API!"

# ----------------------------------------------------
# Single Prediction Endpoint
# ----------------------------------------------------
@superkart_sales_api.post("/v1/predict")
def predict_sales():

    data = request.get_json()

    sample = {
        "Product_Weight": data["Product_Weight"],
        "Product_Sugar_Content": data["Product_Sugar_Content"],
        "Product_Allocated_Area": data["Product_Allocated_Area"],
        "Product_Type": data["Product_Type"],
        "Product_MRP": data["Product_MRP"],
        "Store_Establishment_Year": data["Store_Establishment_Year"],
        "Store_Size": data["Store_Size"],
        "Store_Location_City_Type": data["Store_Location_City_Type"],
        "Store_Type": data["Store_Type"]
    }

    input_data = pd.DataFrame([sample])

    prediction = model.predict(input_data)[0]

    prediction = round(float(prediction), 2)

    return jsonify({
        "Predicted Product Store Sales": prediction
    })

# ----------------------------------------------------
# Batch Prediction Endpoint
# ----------------------------------------------------
@superkart_sales_api.post("/v1/predictbatch")
def predict_sales_batch():

    file = request.files["file"]

    input_data = pd.read_csv(file)

    predictions = model.predict(input_data)

    predictions = [round(float(x), 2) for x in predictions]

    output = {
        "Predicted Sales": predictions
    }

    return jsonify(output)

# ----------------------------------------------------
# Run Flask App
# ----------------------------------------------------
if __name__ == "__main__":
    superkart_sales_api.run(debug=True)
