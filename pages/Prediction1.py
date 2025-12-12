import streamlit as st
import joblib
import pandas as pd
import preprocessing

st.set_page_config(page_title="AcademiCare - ML Modeling")

@st.cache_resource
def load_model():
    return joblib.load("models/model_xgb.pkl")  # change to your file name

model = load_model()

st.title("🎓 Student Dropout Prediction System")
st.write("Fill in the details below to predict the dropout risk.")


with st.form("Student Details"):
    col1, col2, col3 = st.columns(3)

    with col1:
        marital_status = st.selectbox("Marital Status", [
            "Single", "Married", "Divorced", "Facto Union",
            "Legally Separated", "Widower"
        ])

        application_mode = st.selectbox("Application Mode", [
            "1st phase—general contingent",
            "2nd phase—general contingent",
            "Over 23 years old",
            "Change in course",
            "Technological specialization diploma holders",
            "Holders of other higher courses",
            "3rd phase—general contingent",
            "Transfer",
            "Change in institution/course",
            "1st phase—special contingent (Madeira Island)",
            "Short cycle diploma holders",
            "International student (bachelor)",
            "1st phase—special contingent (Azores Island)"
        ])
        
        application_order = st.number_input("Application Order",min_value=1,max_value=9,step=1)

        course_name = st.selectbox("Course Name", [
            "Nursing", "Management", "Social Service", "Veterinary Nursing",
            "Journalism and Communication", "Advertising and Marketing Management",
            "Management (evening attendance)", "Tourism", "Communication Design",
            "Animation and Multimedia Design", "Social Service (evening attendance)",
            "Agronomy", "Basic Education", "Informatics Engineering", "Equiniculture",
            "Oral Hygiene", "Biofuel Production Technologies"
        ])

        age = st.slider("Age at Enrollment",min_value=17,max_value=70,step=1,format="%d")

        prev_qualification = st.selectbox("Previous Qualification", [
            "Secondary education", "Technological specialization course",
            "Basic education 3rd cycle", "Higher education—degree",
            "Other—11th year", "Higher education—degree (1st cycle)",
            "Professional higher technical course", "Higher education—bachelor’s degree",
            "Frequency of higher education", "12th year—not completed",
            "Higher education—master’s degree", "Basic education 2nd cycle",
            "Higher education—master’s (2nd cycle)", "11th year—not completed",
            "10th year—not completed", "Higher education—doctorate", "10th year"
        ])

        father_occ = st.selectbox("Father's Occupation", [
            "Unskilled Workers", "Skilled Industry Workers", "Service/Sales/Security",
            "Administrative Staff", "Technicians & Professionals", "Machine Operators",
            "Armed Forces", "Farmers/Ag Workers", "Scientific Specialists",
            "Legislative/Executive Officers", "Student", "Other Situation", "Blank",
            "Unskilled Industry/Transport", "Other Admin Support", "Construction Workers",
            "Unskilled Ag Workers", "Subsistence Farmers", "Other Armed Forces",
            "Food/Clothing/Other Crafts"
        ])

    with col2:
        attendance = st.selectbox("Daytime/Evening Attendance", ["Daytime", "Evening"])
        displaced = st.selectbox("Displaced Student", ["Yes", "No"])
        is_debtor = st.selectbox("Is Debtor", ["Yes", "No"])
        tuition_up_to_date = st.selectbox("Tuition Fees Up-to-Date", ["Yes", "No"])
        gender = st.selectbox("Gender", ["Male", "Female"])
        scholarship = st.selectbox("Scholarship Holder", ["Yes", "No"])

    with st.expander("📊 Academic & Economic Data"):
        credited_1st = st.number_input("Credited Units (1st Sem)", min_value=0, max_value=50, step=1)
        enrolled_1st = st.number_input("Enrolled Units (1st Sem)", min_value=0, max_value=50, step=1)
        evaluated_1st = st.number_input("Evaluated Units (1st Sem)", min_value=0, max_value=50, step=1)
        approved_1st = st.number_input("Approved Units (1st Sem)", min_value=0, max_value=50, step=1)
        avg_grade_1st = st.number_input("Average Grade (1st Sem)", min_value=0.0, max_value=20.0, step=0.1)
        not_eval_1st = st.number_input("Not Evaluated Units (1st Sem)", min_value=0, max_value=50, step=1)

        credited_2nd = st.number_input("Credited Units (2nd Sem)", min_value=0, max_value=50, step=1)
        enrolled_2nd = st.number_input("Enrolled Units (2nd Sem)", min_value=0, max_value=50, step=1)
        evaluated_2nd = st.number_input("Evaluated Units (2nd Sem)", min_value=0, max_value=50, step=1)
        approved_2nd = st.number_input("Approved Units (2nd Sem)", min_value=0, max_value=50, step=1)
        avg_grade_2nd = st.number_input("Average Grade (2nd Sem)", min_value=0.0, max_value=20.0, step=0.1)
        not_eval_2nd = st.number_input("Not Evaluated Units (2nd Sem)", min_value=0, max_value=50, step=1)

        unemployment_rate = st.number_input("Unemployment Rate (%)", min_value=7.5, max_value=16.5, step=0.1)
        inflation_rate = st.number_input("Inflation Rate (%)", min_value=-1.0, max_value=4.0, step=0.1)
        gdp_per_capita = st.number_input("GDP per Capita (USD)", min_value=-4.0, max_value=3.5, step=0.1)




    submitted = st.form_submit_button("Predict Dropout Risk")

if submitted:

    input_data = pd.DataFrame([{
        "Marital Status": marital_status,
        "Application Mode": application_mode,
        "Application Order":application_order,
        "Course Name": course_name,
        "Daytime/Evening Attendance": attendance,
        "Previous Qualification": prev_qualification,
        "Father's Occupation": father_occ,
        "Displaced Student": displaced,
        "Is Debtor": is_debtor,
        "Tuition Fees Up-to-Date": tuition_up_to_date,
        "Scholarship Holder": scholarship,
        "Age": age,
        "Credited Units (1st Sem)": credited_1st,
        "Enrolled Units (1st Sem)": enrolled_1st,
        "Evaluated Units (1st Sem)": evaluated_1st,
        "Approved Units (1st Sem)": approved_1st,
        "Average Grade (1st Sem)": avg_grade_1st,
        "Not Evaluated Units (1st Sem)": not_eval_1st,
        "Credited Units (2nd Sem)": credited_2nd,
        "Enrolled Units (2nd Sem)": enrolled_2nd,
        "Evaluated Units (2nd Sem)": evaluated_2nd,
        "Approved Units (2nd Sem)": approved_2nd,
        "Average Grade (2nd Sem)": avg_grade_2nd,
        "Not Evaluated Units (2nd Sem)": not_eval_2nd,
        "Unemployment Rate (%)": unemployment_rate,
        "Inflation Rate (%)": inflation_rate,
        "GDP per Capita (USD)": gdp_per_capita,
        "Gender":gender

    }])


    try:
        X_processed = preprocessing.transform(input_data)
        prediction = model.predict(X_processed)
        if(prediction==0): 
            result = "Dropout"
            st.error(f"⚠ High Dropout Risk")
            st.write("### 📌 Recommendation:")
            st.write("- Provide academic counseling")
            st.write("- Offer extra tutoring sessions")
            st.write("- Monitor attendance closely")            
        elif(prediction==1):
            result = "Currently Enrolled"
            st.success(f"✅ Low Dropout Risk")
            st.write("### 📌 Keep up the good work!")
            st.write("- Encourage participation")
            st.write("- Maintain academic performance")  
        else:
            result="Graduated"
            st.success(f"✅ Very likely to graduate")
            st.write("Good Work")      
    except Exception as e:
        st.error(f"⚠️ Error during prediction: {e}")



if st.button("Ask AI→"):
    st.switch_page("pages/AI_assistant.py")        

# if st.button("Predict Dropout Risk"):
#     prediction = model.predict(input_df)[0]
#     probability = model.predict_proba(input_df)[0][1]  # Probability of dropout

#     if prediction == 1:
#         st.error(f"⚠ High Dropout Risk — Probability: {probability:.2%}")
#     else:
        # st.success(f"✅ Low Dropout Risk — Probability: {probability:.2%}")


