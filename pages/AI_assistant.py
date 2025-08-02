import streamlit as st
from groq import Groq
import os
from dotenv import load_dotenv

st.set_page_config(page_title="AcademiCare - AI Assistant")

# Load environment variables
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

client = Groq(api_key=api_key)

st.title("🤖 AI Assistant - AcademiCare")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "I am an AI assistant for a student dropout prediction system. Provide insights, explain results, and suggest interventions to reduce dropout rates."}
    ]

user_input = st.chat_input("Ask your question about dropout prediction or interventions...")

# Display chat history (excluding system prompt)
for msg in st.session_state.messages[1:]:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if user_input:
    st.chat_message("user").markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("assistant"):
        response_holder = st.empty()
        collected_response = ""

        completion = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=st.session_state.messages,
            stream=True,
        )
        for chunk in completion:
            if chunk.choices[0].delta.content:
                collected_response += chunk.choices[0].delta.content
                response_holder.markdown(collected_response)

        st.session_state.messages.append({"role": "assistant", "content": collected_response})
