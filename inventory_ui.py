import streamlit as st
import pandas as pd
from joblib import load

st.title("📦 Inventory Prediction Dashboard")

# Take user inputs for all required features
stock_level = st.number_input("Enter Stock Level:")
procured_quantity = st.number_input("Enter Procured Quantity:")
unit_price = st.number_input("Enter Unit Selling Price:")
stock_to_order_ratio = st.number_input("Enter Stock to Order Ratio:")
total_spent = st.number_input("Enter Total Spent:")
discount_percent = st.number_input("Enter Discount Percent:")

# Load model and make prediction
if st.button("Predict Stock Status"):
    model = load("logistic_model.pkl")
    input_data = [[stock_level, procured_quantity, unit_price,
                   stock_to_order_ratio, total_spent, discount_percent]]
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("❌ Out of Stock Risk")
    else:
        st.success("✅ In Stock")
