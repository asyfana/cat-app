import streamlit as st
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json

st.title("🐱 Cat Database Viewer")
st.markdown("Explore cat data from Google Sheets")

# Google Sheets authentication
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

# Load credentials from Streamlit secrets
creds_dict = st.secrets["gcp_service_account"]
credentials = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
client = gspread.authorize(credentials)

# Open Google Sheet
sheet = client.open("Cat_Data").sheet1  # Your sheet name
data = sheet.get_all_records()

# Convert to DataFrame
df = pd.DataFrame(data)

# Display
st.dataframe(df)

# Optional filter
if st.checkbox("Filter by breed"):
    breed = st.selectbox("Choose a breed", df['Breed'].unique())
    st.write(df[df['Breed'] == breed])


