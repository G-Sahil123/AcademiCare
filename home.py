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

    
# import streamlit as st
# import io

# def help(code):
#     st.session_state.code_to_explain = code
#     st.session_state.chat_mode = "code_explanation"
#     st.switch_page("pages/4_AI_Assistant.py")
    

# st.set_page_config(page_title="DataPilot - Data Exploration")

# st.title("🔍 Data Exploration")

# if "df" not in st.session_state:
#     st.warning("Please upload a dataset first from the Home page.")
#     st.stop()

# df = st.session_state.df
# st.markdown("### Preview of Dataset")
# code1 = """
#         df.sample(7)
#         """
# st.code(code1,language="python")
# st.dataframe(df.sample(7))

# if st.button("💬 Explain this code with AI",key="explain_sample"):
#     help(code1)

# st.markdown("### Columns ")
# st.markdown("> Ignore the extra count column it is used in data visualization")
# # List of columns to drop
# cols_to_drop = [
#     'CLIENTNUM',
#     'Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_1',
#     'Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_2'
# ]

# # Store original code for AI explanation
# code2 = f"""
# # Drop unnecessary columns
# df.drop(columns={cols_to_drop}, inplace=True)
# df.columns
# """
# st.code(code2, language="python")

# # Drop only columns that exist in the DataFrame
# existing_cols_to_drop = [col for col in cols_to_drop if col in df.columns]
# df.drop(columns=existing_cols_to_drop, inplace=True)

# # Show updated columns
# st.dataframe(df.columns)

# # AI explanation button
# if st.button("💬 Explain this code with AI", key="explain_columns"):
#     help(code2)


# st.markdown("### Column Description")
# st.markdown("""
# ### 🧾 Credit Card Customers Dataset 

# This document provides a description of each column in the dataset to assist with understanding and analysis.

# ---

# ### 🎯 Target Column
# - **Attrition_Flag**: Whether the customer has churned (Closed Account) or is an Existing Customer.

# ---

# ### 🧑 Customer Demographics
# - **Customer_Age**: Age of the customer (numeric).
# - **Gender**: Gender of the customer (`M` or `F`).
# - **Dependent_count**: Number of dependents the customer has (integer).
# - **Education_Level**: Education level of the customer (e.g., High School, Graduate, Doctorate).
# - **Marital_Status**: Marital status (e.g., Married, Single, Divorced).
# - **Income_Category**: Annual income category (e.g., Less than \$40K, \$60K - \$80K).
# - **Card_Category**: Type of credit card held (e.g., Blue, Silver, Gold, Platinum).

# ---

# ### 🏦 Account & Credit Information
# - **Months_on_book**: Total duration of the account in months.
# - **Total_Relationship_Count**: Total number of products held by the customer.
# - **Months_Inactive_12_mon**: Number of months inactive in the last 12 months.
# - **Contacts_Count_12_mon**: Number of customer contacts in the last 12 months.

# ---

# ### 💳 Transaction Behavior
# - **Credit_Limit**: Credit limit on the credit card account.
# - **Total_Revolving_Bal**: Balance that is carried from one month to the next.
# - **Avg_Open_To_Buy**: Average amount of credit available for making purchases.
# - **Total_Amt_Chng_Q4_Q1**: Ratio of total transaction amount in Q4 compared to Q1.
# - **Total_Trans_Amt**: Total transaction amount in the last 12 months.
# - **Total_Trans_Ct**: Total number of transactions in the last 12 months.
# - **Total_Ct_Chng_Q4_Q1**: Ratio of transaction count in Q4 compared to Q1.
# - **Avg_Utilization_Ratio**: Average utilization ratio of the credit card.
# """
# )

# st.markdown("### Shape of Dataset")
# code3 = """
#         df.shape
#         """
# st.code(code3,language="python")
# st.markdown("Shape: {}".format(df.shape))

# if st.button("💬 Explain this code with AI",key="explain_shape"):
#     help(code3)

# st.markdown("### Info of Dataset")
# code4 = """
#         df.info()
#         """
# st.code(code4,language="python")
# buffer = io.StringIO()
# df.info(buf=buffer)
# info_str = buffer.getvalue()
# st.text(info_str)

# if st.button("💬 Explain this code with AI",key="explain_info"):
#     help(code4)

# st.markdown("### Numerical Column Analysis")
# code5 = """
#         df.describe()
#         """
# st.code(code5,language="python")
# st.dataframe(df.describe())
# if st.button("💬 Explain this code with AI",key="explain_describe"):
#     help(code5)

# st.markdown("### Null Values in Dataset")
# code6 = """
#         df.isnull().sum()
#         """
# st.code(code6,language="python")
# st.dataframe(df.isnull().sum())
# if st.button("💬 Explain this code with AI",key="explain_null_count"):
#     help(code6)
