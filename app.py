import streamlit as st
import joblib
from sklearn.linear_model import LinearRegression
import pandas as pd


model = joblib.load("model.pkl")

st.title("Loan Eligibility Predictor")

st.write("Provide us your detail to let us predict your Loan status")

gender = st.selectbox("Gender", ["Male", "Female"])
married = st.selectbox("Married", ["Yes", "No"])
dependents = st.selectbox("Dependents", ["0", "1", "2", "3+"])
education = st.selectbox("Education", ["Graduate", "Not Graduate"])
self_employed = st.selectbox("Self Employed", ["Yes", "No"])
applicant_income = st.number_input("Annual Applicant Income(in thousands)", min_value=0)
coapplicant_income = st.number_input("Annual Coapplicant Income (in thousands)", min_value=0)
loan_amount = st.number_input("Loan Amount (in thousands)", min_value=0)
loan_term = st.selectbox("Loan Amount Term (in months)", [360, 180, 120, 60])
credit_history = st.selectbox("Credit History", [1.0, 0.0])
property_area = st.selectbox("Property Area", ["Urban", "Semiurban", "Rural"])


gender = 1 if gender == "Male" else 0
married = 1 if married == "Yes" else 0
education = 1 if education == "Graduate" else 0
self_employed = 1 if self_employed == "Yes" else 0
dependents = 4 if dependents == "3+" else int(dependents)
property_area = 2 if property_area == "Urban" else (1 if property_area == "Semiurban" else 0)


# Prediction
if st.button("Check Eligibility"):
    # Create DataFrame
    input_data = pd.DataFrame({
        "Gender": [gender],
        "Married": [married],
        "Dependents": [dependents],
        "Education": [education],
        "Self_Employed": [self_employed],
        "ApplicantIncome": [applicant_income],
        "CoapplicantIncome": [coapplicant_income],
        "LoanAmount": [loan_amount],
        "Loan_Amount_Term": [loan_term],
        "Credit_History": [credit_history],
        "Property_Area": [property_area]
    })
    
    # Preprocess input
    prediction = model.predict(input_data)
    
    # Display result
    if prediction[0] == 1:
        st.success("Congratulations! You are eligible for the loan.")
    else:
        st.error("Sorry, you are not eligible for the loan.")

