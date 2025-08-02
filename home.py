import streamlit as st
from dotenv import load_dotenv

st.set_page_config(
    page_title="AcademiCare - Introduction",
    page_icon="🎓",
    layout="centered"    
)

load_dotenv()

#st.title("🎓 Welcome to AcademiCare")


st.markdown(
    """
    🎓 Show that you care - Welcome to AcademiCare

    This application helps in predicting the **likelihood of a student dropping out** based on academic and demographic data.
    Which helps in identifying which student needs required efforts and  help which they need. 
    
    Please click on the button below to make identify who needs care.
    """
)


st.sidebar.header("About")
st.sidebar.markdown(
    """
    **Student Dropout Prediction System**  
    - ML-powered prediction  
    - Helps identify at-risk students  
    - Integrated with AI assistant  
    """
)

if st.button("Make Prediction →"):
    st.switch_page("pages/Prediction.py")


