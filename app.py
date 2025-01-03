# -*- coding: utf-8 -*-
import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# set page configuration
st.set_page_config(page_title = "Health Gaurd", layout = "wide", page_icon = "🧑‍⚕️")

# path of working directory
working_dir = os.path.dirname(os.path.abspath(__file__))

# loading of the save model
diabetes_model = pickle.load(open('diabetes_SVM/diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open('heart_disease_LogisticRegression\heart_disease_model.sav', 'rb'))
parkinsons_model = pickle.load(open('parkinsons_SVM/parkinsons_model.sav', 'rb'))

# sidebar for navigation
with st.sidebar:
    selected = option_menu("Multiple Disease Prediction System", ["Diabetes Disease Prediction", "Heart Disease Prediction", "Parkinson's Disease Prediction", "Breast Cancer Prediction"], menu_icon = "hospital-fill", icons = ["activity", "heart", "person",], default_index = 0)

# diabetes prediction page
if selected == "Diabetes Disease Prediction":

    # page title
    st.title("Diabetes Prdiction Using ML")

    # getting input data from the user
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        pregnancies = st.text_input("Number of Pregnancies")
        insulin = st.text_input("Insulin Level")

    with col2:
        glucose = st.text_input("Glucose Level")
        bmi = st.text_input("BMI Value")

    with col3:
        blood_pressure = st.text_input("Blood Pressure Value")
        dpf = st.text_input("Diabetes Pedigree Function Value")

    with col4:
        skin_thickness = st.text_input("Skin Thickness Value")
        age = st.text_input("Person Age")

    # backend logic
    diab_diagnosis = ""

    # creation of a button
    if st.button("Diabetes Text Result"):
        try:
            # Collect inputs and check for empty strings or None
            user_input = [pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, dpf, age]
            if any(x == '' or x is None for x in user_input):
                st.error("All fields are required. Please provide valid inputs.")
            else:
                # Convert inputs to float
                user_input = [float(x) for x in user_input]

                # Make prediction
                diabetes_prediction = diabetes_model.predict([user_input])
                if diabetes_prediction[0] == 1:
                    diab_diagnosis = "Person is Diabetic"
                else:
                    diab_diagnosis = "Person is not Diabetic"

                st.success(diab_diagnosis)
        except ValueError:
            st.error("Invalid input! Ensure all inputs are numeric.")

    
# heart disease prediction page
if selected == "Heart Disease Prediction":

    # page title
    st.title("Heart Disease Prdiction Using ML")

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        age = st.text_input("Age")
        chol = st.text_input("Serum cholertrol in mg/dl")
        exang = st.text_input("Excercise induces angina")
        thal = st.text_input("Thal: 0 => Normal; 1=> fixed defect")

    with col2:
        sex = st.text_input("Gender")
        fbs = st.text_input("Fasting blood sugar")
        oldpeak = st.text_input("ST depression induced by excercise")

    with col3:
        cp = st.text_input("Cheast pain type")
        restecg = st.text_input("Resting electrocardiographic result")
        slope = st.text_input("Slope of the peak excercise ST segment")

    with col4:
        trestbps = st.text_input("Resting blood pressure")
        thalach = st.text_input("Maximum heart rate achieved")
        ca = st.text_input("Major vessels colored by flourosopy")

    # backendlogic
    heart_diagnosis = ""

    # creation of a button
    if st.button("Heart Disease Text Result"):
        try:
            # Collect inputs and check for empty strings
            user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
            if any(x == '' or x is None for x in user_input):
                st.error("All fields are required. Please provide valid inputs.")
            else:
                # Convert inputs to float
                user_input = [float(x) for x in user_input]
                
                # Make prediction
                heart_model_prediction = heart_disease_model.predict([user_input])
                if heart_model_prediction[0] == 1:
                    heart_diagnosis = "Person is Unhealthy"
                else:
                    heart_diagnosis = "Person is Healthy"
                
                st.success(heart_diagnosis)
        except ValueError:
            st.error("Invalid input! Ensure all inputs are numeric.")


# Parkinson's Disease Prediction Page
if selected == "Parkinson's Disease Prediction":

    # Page title
    st.title("Parkinson's Disease Prediction Using ML")

    # Getting input data from the user
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        name = st.text_input("Name of the Patient")
        MDVP_Jitter_percent = st.text_input("MDVP:Jitter(%)")
        Jitter_DDP = st.text_input("Jitter:DDP")
        Shimmer_APQ5 = st.text_input("Shimmer:APQ5")
        HNR = st.text_input("HNR")
        spread2 = st.text_input("Spread2")

    with col2:
        MDVP_Fo_Hz = st.text_input("MDVP:Fo(Hz)")
        MDVP_Jitter_Abs = st.text_input("MDVP:Jitter(Abs)")
        MDVP_Shimmer = st.text_input("MDVP:Shimmer")
        MDVP_APQ = st.text_input("MDVP:APQ")
        RPDE = st.text_input("RPDE")
        D2 = st.text_input("D2")

    with col3:
        MDVP_Fhi_Hz = st.text_input("MDVP:Fhi(Hz)")
        MDVP_RAP = st.text_input("MDVP:RAP")
        MDVP_Shimmer_dB = st.text_input("MDVP:Shimmer(dB)")
        Shimmer_DDA = st.text_input("Shimmer:DDA")
        DFA = st.text_input("DFA")
        PPE = st.text_input("PPE")

    with col4:
        MDVP_Flo_Hz = st.text_input("MDVP:Flo(Hz)")
        MDVP_PPQ = st.text_input("MDVP:PPQ")
        Shimmer_APQ3 = st.text_input("Shimmer:APQ3")
        NHR = st.text_input("NHR")
        spread1 = st.text_input("Spread1")


    # Backend logic
    parkinsons_diagnosis = ""

    # Creation of a button
    if st.button("Parkinson's Disease Text Result"):
        try:
            # Collect inputs and check for empty strings or None
            user_input = [MDVP_Fo_Hz, MDVP_Fhi_Hz, MDVP_Flo_Hz, MDVP_Jitter_percent, MDVP_Jitter_Abs, 
                          MDVP_RAP, MDVP_PPQ, Jitter_DDP, MDVP_Shimmer, MDVP_Shimmer_dB, Shimmer_APQ3, 
                          Shimmer_APQ5, MDVP_APQ, Shimmer_DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]
            
            if any(x == '' or x is None for x in user_input):
                st.error("All fields except 'Name' and 'Status' are required. Please provide valid inputs.")
            else:
                # Convert inputs to float
                user_input = [float(x) for x in user_input]

                # Make prediction
                parkinsons_prediction = parkinsons_model.predict([user_input])
                if parkinsons_prediction[0] == 1:
                    parkinsons_diagnosis = "Person is likely to have Parkinson's Disease."
                else:
                    parkinsons_diagnosis = "Person is not likely to have Parkinson's Disease."

                st.success(parkinsons_diagnosis)
        except ValueError:
            st.error("Invalid input! Ensure all inputs are numeric, except for 'Name' and 'Status'.")


# Breast Cancer Prediction page
if selected == "Breast Cancer Prediction":
    st.title("Breast Cancer Prediction coming soon...")
    st.write("This feature is under development.")