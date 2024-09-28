
import pickle
from ml_model import feature_extraction, model

with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)
from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai
from langchain.schema import HumanMessage, SystemMessage, AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from email_fetcher import get_email_content, save_email_to_file

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
#genai.configure(api_key=os.getenv("AIzaSyDoiOOAYlJn24Uwb6AJoEwG84I2RVeVgfk"))

model1 = ChatGoogleGenerativeAI(model="gemini-pro", convert_system_message_to_human=True)

# Initialize session state for flow messages if not already present
if "flowmessages" not in st.session_state:
    st.session_state["flowmessages"] = []

if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

def classify_email_content(email_content):
    # Use the ML model to predict
    prediction = model.predict([email_content])[0]

    # Map prediction to human-readable labels
    threat_label = "Threat" if prediction == 0 else "Avoidable"

    return threat_label


#def check_email_threat(email_content):
    if '@ac.in' in email_content:
        return 'Threat'
    elif '@gmail.com' in email_content:
        return 'Avoidable'
    else:
        return 'Out of Context'

def get_gemini_response(email_content):
    response = classify_email_content(email_content)
    return response

st.set_page_config("Email Threat Detector")
st.header("Threat Detection")

gmail_username = st.text_input("Gmail Username")
gmail_password = st.text_input("Gmail Password", type="password")

if st.button("Fetch and Classify Emails"):
    # Fetch emails from Gmail
    subject, content = get_email_content(gmail_username, gmail_password, "imap.gmail.com", 993)
    if subject and content:
        # Save the email content to a file
        file_path = save_email_to_file(subject, content)
        st.write(f"Email saved to: {file_path}")

        # Classify the email content using the spam model
        is_spam = get_gemini_response(content)
        st.write(is_spam)
    else:
        st.write("Failed to retrieve email content.")


