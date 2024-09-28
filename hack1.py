from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai
from langchain.schema import HumanMessage, SystemMessage, AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
genai.configure(api_key=os.getenv("AIzaSyDoiOOAYlJn24Uwb6AJoEwG84I2RVeVgfk"))

model = ChatGoogleGenerativeAI(model="gemini-pro", convert_system_message_to_human=True)

# Initialize session state for flow messages if not already present
if "flowmessages" not in st.session_state:
    st.session_state["flowmessages"] = []

if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

def check_email_threat(email_content):
    if '@' in email_content and 'gmail.com' not in email_content:
        return 'Threat'
    elif '@gmail.com' in email_content:
        return 'Avoidable'
    else:
        return 'Out of Context'

def get_gemini_response(email_content):
    response = check_email_threat(email_content)
    return response

st.set_page_config("Email Threat Detector")
st.header("Threat Detection")

email_content = st.text_area("Enter email content:")

if st.button("Classify Email"):
    response = get_gemini_response(email_content)
    st.write(response)
