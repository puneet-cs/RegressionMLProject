# pip install streamlit
# streamlit run main.py

"""
** Last features leftout just before feature scaling  **
** Scaler knows these features only **
'age', 'region', 'number_of_dependants', 'bmi_category', 'income_level',
       'income_lakhs', 'insurance_plan', 'genetical_risk', 'total_risk_score',
       'gender_Male', 'marital_status_Unmarried', 'smoking_status_Occasional',
       'smoking_status_Regular', 'employment_status_Salaried',
       'employment_status_Self-Employed'],

# income_level column is deleted later before training model

"""

import streamlit as st
from prediction_helper import predict

st.title("Health insurance Premium Predictor")


categorical_options = { 
"gender" : ['Male', 'Female'],
"region" : ['Northeast', 'Northwest', 'Southeast', 'Southwest'],
"marital_status" : ['Unmarried', 'Married'],
"bmi_category" : ['Overweight', 'Underweight', 'Normal', 'Obesity'],
"smoking_status" : ['Regular', 'No Smoking', 'Occasional'],
"employment_status" : ['Self-Employed', 'Freelancer', 'Salaried'],
"income_level" : ['> 40L', '<10L', '10L - 25L', '25L - 40L'],
"insurance_plan" : ['Bronze','Silver', 'Gold']
}

# Create four rows of three column each
row1 = st.columns(3)
row2 = st.columns(3)
row3 = st.columns(3)
row4 = st.columns(3)

with row1[0]:
    age = st.number_input('Age', min_value = 18, step= 1, max_value = 100)
with row1[1]:
    region =  st.selectbox('region', categorical_options["region"]  )
with row1[2]:
    number_of_dependents = st.number_input('number of dependents', min_value = 0, step =1, max_value = 20 )
    

with row2[0]:
    bmi_category = st.selectbox('BMI category', categorical_options["bmi_category"]  )
with row2[1]:
    income_lakhs = st.number_input("Income in lakhs", step = 1, min_value = 0, max_value = 200)  
with row2[2]:
    insurance_plan = st.selectbox('Insurance plan', categorical_options["insurance_plan"]  )
    

with row3[0]:
    genetical_risk = st.number_input('Genetical risk', step= 1, max_value = 5)
with row3[1]:
    total_risk_score = st.number_input("Total risk score", step = 1, min_value = 0, max_value = 20)
with row3[2]:
   gender =  st.selectbox('Gender', categorical_options["gender"]  )

with row4[0]:
     marital_status = st.selectbox('Marital status', categorical_options["marital_status"]  )
with row4[1]:
    smoking_status =  st.selectbox('Smoking status', categorical_options["smoking_status"]  )
with row4[2]:
    employment_status = st.selectbox("Employment status", categorical_options["employment_status"])

# Creating a dictionary to store all input values together
input_dict = {
    'age' : age,
    'region' : region,
    'number_of_dependents' : number_of_dependents,
    'bmi_category' : bmi_category,
    'income_lakhs' : income_lakhs,
    'insurance_plan' : insurance_plan,
    'genetical_risk' : genetical_risk,
    'total_risk_score' : total_risk_score,
    'gender' : gender,
    'marital_status' : marital_status,
    'smoking_status' : smoking_status,
    'employment_status' : employment_status
}

if st.button('Predict'):
    prediction = predict(input_dict)
    st.success(f"Predicted Health insurance premium: {prediction}")
