
import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load trained model
model = joblib.load("best_model.pkl")   # Replace with your saved model name

st.title("SuperKart Sales Prediction")
st.write("Enter the product and store details to predict product sales.")

# -----------------------------
# User Inputs
# -----------------------------
Product_Weight = st.number_input(
    "Product Weight",
    min_value=0.0,
    value=12.5,
    step=0.1
)

Product_Sugar_Content = st.selectbox(
    "Product Sugar Content",
    ["Low Sugar", "Regular", "No Sugar"]
)

Product_Allocated_Area = st.number_input(
    "Product Allocated Area",
    min_value=0.0,
    value=150.0,
    step=1.0
)

Product_Type = st.selectbox(
    "Product Type",
    [
        "Fruits and Vegetables",
        "Snack Foods",
        "Frozen Foods",
        "Dairy",
        "Household",
        "Baking Goods",
        "Canned",
        "Health and Hygiene",
        "Meat",
        "Soft Drinks",
        "Breads",
        "Hard Drinks",
        "Others",
        "Starchy Foods",
        "Breakfast",
        "Seafood"
    ]
)

Product_MRP = st.number_input(
    "Product MRP",
    min_value=0.0,
    value=150.0,
    step=1.0
)

Store_Establishment_Year = st.number_input(
    "Store Establishment Year",
    min_value=1980,
    max_value=2025,
    value=2005,
    step=1
)

Store_Size = st.selectbox(
    "Store Size",
    ["Small", "Medium", "High"]
)

Store_Location_City_Type = st.selectbox(
    "Store Location",
    ["Tier 1", "Tier 2", "Tier 3"]
)

Store_Type = st.selectbox(
    "Store Type",
    [
        "Supermarket Type1",
        "Supermarket Type2",
        "Departmental Store",
        "Food Mart"
    ]
)

# -----------------------------
# Create Input DataFrame
# -----------------------------
input_data = pd.DataFrame([{
    "Product_Weight": Product_Weight,
    "Product_Sugar_Content": Product_Sugar_Content,
    "Product_Allocated_Area": Product_Allocated_Area,
    "Product_Type": Product_Type,
    "Product_MRP": Product_MRP,
    "Store_Establishment_Year": Store_Establishment_Year,
    "Store_Size": Store_Size,
    "Store_Location_City_Type": Store_Location_City_Type,
    "Store_Type": Store_Type
}])

# -----------------------------
# Prediction
# -----------------------------
if st.button("Predict Sales"):
    prediction = model.predict(input_data)

    st.success(f"Predicted Sales: ${prediction[0]:,.2f}")
