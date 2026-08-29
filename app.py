
import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("car_price_model (1).pkl")

st.set_page_config(
    page_title="Car Price Predictor",
    page_icon="🚗"
)

st.title("🚗 Car Price Prediction System")
st.write("Enter car details to estimate its price.")

st.divider()

year = st.number_input(
    "Manufacturing Year",
    min_value=2000,
    max_value=2026,
    value=2020
)

mileage = st.number_input(
    "Mileage (km)",
    min_value=0,
    max_value=300000,
    value=30000
)

engine = st.number_input(
    "Engine Size (CC)",
    min_value=500,
    max_value=5000,
    value=1500
)

owners = st.number_input(
    "Previous Owners",
    min_value=0,
    max_value=10,
    value=1
)

if st.button("Predict Car Price 🚘"):

    input_data = pd.DataFrame({
        "Year": [year],
        "Mileage": [mileage],
        "Engine_CC": [engine],
        "Previous_Owners": [owners]
    })

    prediction = model.predict(input_data)[0]

    st.success(
        f"Estimated Car Price: Rs. {prediction:,.0f}"
    )
