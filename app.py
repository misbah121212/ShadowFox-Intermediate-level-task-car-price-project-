import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("models/car_price_model.joblib")

st.title("Car Price Prediction App")

# Inputs
year = st.number_input("Year of Purchase", 2000, 2025)
present_price = st.number_input("Present Price (in lakhs)")
kms_driven = st.number_input("KMs Driven")
owner = st.selectbox("Number of Previous Owners", [0, 1, 2])
fuel_type = st.selectbox("Fuel Type", ["Petrol", "Diesel", "CNG"])
seller_type = st.selectbox("Seller Type", ["Dealer", "Individual"])
transmission = st.selectbox("Transmission", ["Manual", "Automatic"])

if st.button("Predict Price"):
    # Prepare input
    input_df = pd.DataFrame([{
        'Year': year,
        'Present_Price': present_price,
        'Kms_Driven': kms_driven,
        'Owner': owner,
        'Fuel_Type': fuel_type,
        'Seller_Type': seller_type,
        'Transmission': transmission
    }])
    
    # Prediction
    prediction = model.predict(input_df)[0]
    st.success(f"Predicted Selling Price: {prediction:.2f} lakhs")
