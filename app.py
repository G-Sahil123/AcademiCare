import streamlit as st
import pandas as pd
import pickle
import os
from dotenv import load_dotenv

from groq import Groq  # ← GROQ CLIENT

load_dotenv()

# Initialize Groq Client
api_key = st.secrets["GROQ_API_KEY"]
groq_client = Groq(api_key=api_key)

st.set_page_config(page_title="Dropout Prediction", layout="wide")
st.title("Student Dropout Prediction App")

model = pickle.load(open("model.pkl", "rb"))
feature_columns = pickle.load(open("feature_columns.pkl", "rb"))

# Preprocessing
edu_map = {'Unknown': 0, 'Basic': 1, 'Secondary_Incomplete': 2, 'Secondary/Technical': 3, 'HigherEd': 4, 'Doctorate': 5}
occ_map = {'Unemployed': 0, 'LowSkill': 1, 'Skilled': 2, 'Technical': 3, 'Professional': 4, 'ArmedForces': 5}
load_map = {'Low Load': 0, 'Medium Load': 1, 'Full Load': 2}

attendance_options = ["Daytime", "Evening"]
course_options = ["Arts", "Communication", "Education", "Energy", "Engineering",
                  "Health", "Management", "Social"]
marital_options = ["Married", "Separated/Divorced", "Single", "Widowed"]
appmode_options = ["International", "Ordinance", "SpecialRegional", "Transfer/Other", "Unknown"]
nationality_options = ["Portuguese", "Europe", "SouthAmerica"]

# Input
st.subheader("Enter Student Details")

inputs = {}

# Personal Information
with st.expander(" Personal Information", expanded=True):
    col1, col2 = st.columns(2)
    with col1:
        inputs['Gender (1=Male, 0=Female)'] = st.number_input("Gender of Student", 0, 1, 0)
        inputs['Age at Enrollment'] = st.number_input("Age of student at enrollment", 0, 100, 18)
        selected_marital = st.selectbox("Student's marital status", marital_options)
        for opt in marital_options:
            inputs[f"MaritalStatus_Simple_{opt}"] = 1 if opt == selected_marital else 0
    with col2:
        inputs['International Student'] = st.number_input("Is International Student", 0, 1, 0)
        selected_nat = st.selectbox("Nationality", nationality_options)
        for opt in nationality_options:
            inputs[f"Nationality_Simple_{opt}"] = 1 if opt == selected_nat else 0

# Parent's Information
with st.expander("Parent Education & Occupation", expanded=True):
    col1, col2 = st.columns(2)
    with col1:
        inputs['FatherQual'] = edu_map[st.selectbox("Highest education of father", list(edu_map.keys()))]
        inputs['MotherQual'] = edu_map[st.selectbox("Highest education of mother", list(edu_map.keys()))]
    with col2:
        inputs['FatherOcc_Simple'] = occ_map[st.selectbox("Father Occupation ", list(occ_map.keys()))]
        inputs['MotherOcc_Simple'] = occ_map[st.selectbox("Mother Occupation ", list(occ_map.keys()))]

# Financial Information
with st.expander("Financial Information", expanded=True):
    col1, col2 = st.columns(2)
    with col1:
        inputs['Debt Risk'] = st.number_input("Is student has debt", 0, 1, 0)
        inputs['Tuition Stable'] = st.number_input("Is tuition is up-to-date", 0, 1, 1)
        inputs['Financial Hardship'] = st.number_input("Financial Hardship - (General financial difficulties)", 0.0, 10.0, 0.0)
    with col2:
        inputs['Socioeconomic Stress Score'] = st.number_input("Socioeconomic Stress Score - (Socioeconomic pressure)", 0.0, 10.0, 0.0)
        inputs['Econ_Disadvantage'] = st.number_input("Economic Disadvantage - (Level of economic disadvantage)", 0.0, 4.0, 0.0)

# Academic Performance
with st.expander("Academic Performance", expanded=True):
    col1, col2 = st.columns(2)
    with col1:
        inputs['Pass Rate (1st Sem)'] = st.number_input("Pass Rate (1st Sem) - Fraction of courses passed 1st sem", 0.0, 1.0, 0.5)
        inputs['Pass Rate (2nd Sem)'] = st.number_input("Pass Rate (2nd Sem) - Fraction of courses passed 2nd sem", 0.0, 1.0, 0.5)
    with col2:
        inputs['Load Category'] = load_map[st.selectbox("Load Category - Full/Medium/Low course load", list(load_map.keys()))]
        inputs['Grade Difference'] = st.number_input("Grade Difference - 2nd Sem grade minus 1st Sem grade", -20.0, 20.0, 0.0)

# Other Fields
with st.expander("Other Categorical Fields", expanded=True):
    inputs['Daytime/Evening Attendance_Evening'] = 1 if st.selectbox("Attendance - Daytime or Evening", attendance_options) == "Evening" else 0
    selected_course = st.selectbox("Course Field - Student's course of study", course_options)
    for opt in course_options:
        inputs[f"Course_Field_{opt}"] = 1 if opt == selected_course else 0
    selected_appmode = st.selectbox("Application Mode - How student applied", appmode_options)
    for opt in appmode_options:
        inputs[f"ApplicationMode_Simple_{opt}"] = 1 if opt == selected_appmode else 0
    inputs['ApplicationOrder_Simple'] = st.number_input("Application Order - Sequence of application", 1, 10, 1)
    inputs['Displaced Student'] = st.number_input("Displaced Student (0/1) - 1 if relocated", 0, 1, 0)

# Create DataFrame
data_df = pd.DataFrame([{col: inputs.get(col, 0) for col in feature_columns}])

# Prediction Button
if st.button("Predict Dropout"):
    pred = model.predict(data_df)[0]
    st.session_state['prediction'] = pred

    # ---- DISPLAY RESULT ----
    if pred == 1:
        st.markdown("""
            <div style="
                text-align: center;
                background-color: #ffe6e6;
                padding: 30px;
                border-radius: 20px;
                color: #b30000;
                font-size: 26px;
                font-weight: bold;
                box-shadow: 5px 5px 20px rgba(0,0,0,0.3);
            ">
                Prediction: Dropout <br>
                The model indicates this student is at risk of dropping out.
            </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
            <div style="
                text-align: center;
                background-color: #e6ffe6;
                padding: 30px;
                border-radius: 20px;
                color: #006600;
                font-size: 26px;
                font-weight: bold;
                box-shadow: 5px 5px 20px rgba(0,0,0,0.3);
            ">
                Prediction: Graduate <br>
                The model predicts this student is likely to graduate successfully!
            </div>
        """, unsafe_allow_html=True)

    # ---- AI EXPLANATION USING GROQ ----
    prompt = f"""
You are an academic advisor. A student has the following features:
{data_df.iloc[0].to_dict()}

Model's Feature Importance: {model.feature_importances_}
Model Parameters: {model.get_params()}
Model predicted: {"Dropout" if pred==1 else "Graduate"}

Provide:
1. Why this prediction happened.
2. Actionable advice to prevent dropout (if any).
3. Three "What-if" scenarios:  
   → Example: What if pass rate improves?  
   → What if financial stress decreases?  
   → What if load category changes?
Respond clearly in bullet points.
"""

    groq_response = groq_client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": "You are a helpful and supportive academic advisor."},
            {"role": "user", "content": prompt},
        ],
        temperature=0.6,
    )

    explanation = groq_response.choices[0].message.content

    # Display Response
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown(
        f"""
        <div style="
            background-color: #f0f8ff;
            padding: 25px;
            border-radius: 20px;
            color: #003366;
            font-size: 20px;
            font-weight: 500;
            line-height: 1.6;
            box-shadow: 3px 3px 15px rgba(0,0,0,0.2);
        ">
            <strong>Explanation & Advice:</strong><br><br>
            {explanation}
        </div>
        """,
        unsafe_allow_html=True
    )
