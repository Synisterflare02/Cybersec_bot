import streamlit as st
import pandas as pd

# Sample data for threat feeds and infrastructure
threats = pd.DataFrame({
    'Threat ID': ['T001', 'T002', 'T003'],
    'Description': ['Remote code execution vulnerability', 'Denial of service attack', 'Data breach'],
    'Severity': ['High', 'Medium', 'High']
})

infrastructure = pd.DataFrame({
    'Asset ID': ['A001', 'A002', 'A003'],
    'Asset Type': ['Server', 'Network', 'Application'],
    'Software': ['Apache 2.4.41', 'Cisco IOS 15.6', 'WordPress 5.7']
})

# Mapping threats to infrastructure
threat_mapping = pd.DataFrame({
    'Threat ID': ['T001', 'T002', 'T003'],
    'Affected Assets': [['A001'], ['A002'], ['A003']]
})

# Streamlit app
st.title('Threat Feed Analysis and Reporting')

# Display threat feeds
st.header('Threat Feeds')
st.write(threats)

# Display infrastructure
st.header('Infrastructure Landscape')
st.write(infrastructure)

# Display threat mapping
st.header('Threat Mapping')
st.write(threat_mapping)

# Generate actionable report
st.header('Actionable Report')
for index, row in threat_mapping.iterrows():
    threat_id = row['Threat ID']
    affected_assets = row['Affected Assets']
    threat_description = threats.loc[threats['Threat ID'] == threat_id, 'Description'].values[0]
    threat_severity = threats.loc[threats['Threat ID'] == threat_id, 'Severity'].values[0]

    st.subheader(f'Threat ID: {threat_id}')
    st.write(f'Description: {threat_description}')
    st.write(f'Severity: {threat_severity}')
    st.write('Affected Assets:')
    for asset_id in affected_assets:
        asset_details = infrastructure.loc[infrastructure['Asset ID'] == asset_id, ['Asset Type', 'Software']].values[0]
        st.write(f'- {asset_id} ({asset_details[0]}, {asset_details[1]})')

    # Provide recommendations based on threat and affected assets
    if threat_severity == 'High':
        st.warning('Recommended Action: Immediate mitigation or remediation required.')
    else:
        st.info('Recommended Action: Assess risk and implement appropriate security controls.')

# Button to escalate unresolved issues
if st.button('Escalate Unresolved Issues'):
    st.warning('Escalation process initiated. Security and infrastructure teams notified.')