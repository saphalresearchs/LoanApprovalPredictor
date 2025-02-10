# Loan Eligibility Prediction System

## Overview
This is a Streamlit-based web application that predicts whether an applicant is eligible for a loan based on various input features. The model uses pre-trained machine learning algorithms to make predictions.

## Features
- User-friendly interface for entering applicant details
- Preprocessing of categorical data into numerical format
- Real-time loan eligibility prediction
- Supports multiple loan-related features

## Technologies Used
- Python
- Streamlit
- Scikit-learn
- Pandas
- NumPy
- Pickle (for model storage)


## Model Details
- The model uses categorical encoding to convert text inputs into numerical values.
- The trained model is stored in `model.pkl`.
- The input features include:
  - Gender
  - Marital Status
  - Dependents
  - Education
  - Self Employed
  - Applicant Income
  - Coapplicant Income
  - Loan Amount
  - Loan Term
  - Credit History
  - Property Area


