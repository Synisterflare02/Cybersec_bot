import os
import streamlit as st
from langchain.schema import HumanMessage, SystemMessage, AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI


GOOGLE_API_KEY = "AIzaSyDDCXh0ZcNIQlIn3Jq1uTjhq7w0vSOZIzU"

# Function to interact with Google Generative AI
def generate_response(prompt):
    # Specify the model parameter based on the available Google AI models
    model = "gemini-pro"  
    # Initialize ChatGoogleGenerativeAI with API key and model
    chat_model = ChatGoogleGenerativeAI(google_api_key=GOOGLE_API_KEY, model=model, convert_system_message_to_human=True)
    # Generate response using the invoke method
    response = chat_model.invoke(prompt)
    return response

# Streamlit app
st.title('Threat Feed Analysis and Reporting')

# Collect threat feed from the user
threat_feed = st.text_input("Enter Threat Feed")

if threat_feed:
    # Determine the severity based on the threat feed
    if "critical" in threat_feed.lower():
        severity = "High"
    elif "warning" in threat_feed.lower():
        severity = "Medium"
    else:
        severity = "Low"

    st.header(f'Threat Feed: {threat_feed}')
    st.write(f'Severity: {severity}')

    # Provide recommendations based on threat severity
    if severity == 'High':
        st.warning('Recommended Action: Immediate mitigation or remediation required.')

        # Collect infrastructure details from the user
        st.header("Enter Infrastructure Details")
        with st.form("infrastructure_form"):
            asset_id = st.text_input("Asset ID")
            asset_type = st.text_input("Asset Type")
            asset_software = st.text_input("Software")
            submit_infrastructure = st.form_submit_button("Submit Infrastructure")

        if submit_infrastructure:
            st.write(f'Affected Asset: {asset_id} ({asset_type}, {asset_software})')

            # Generate response using Google Generative AI
            prompt = f"Generate recommended steps to resolve the following high severity threat: '{threat_feed}' for the affected asset: {HumanMessage(content=f'Asset ID: {asset_id}, Asset Type: {asset_type}, Software: {asset_software}')}."
            response = generate_response(prompt)
            st.write(response)
    elif severity == 'Medium':
        st.info('Recommended Action: Assess risk and implement appropriate security controls.')

        # Generate response using Google Generative AI
        prompt = f"Generate recommended steps to address the following medium severity threat: '{threat_feed}'."
        response = generate_response(prompt)
        st.write(response)
    else:
        st.info('Recommended Action: Monitor the situation and implement basic security best practices.')

        # Generate response using Google Generative AI
        prompt = f"Generate recommended steps to handle the following low severity threat: '{threat_feed}'."
        response = generate_response(prompt)
        st.write(response)

    # Button to escalate unresolved issues
    if st.button('Escalate Unresolved Issues'):
        st.warning('Escalation process initiated. Security and infrastructure teams notified.')