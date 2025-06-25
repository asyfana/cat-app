import streamlit as st
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Set up Streamlit
st.title("🐱 Cat Database Viewer")
st.markdown("View and explore data of cats from a connected Google Sheet.")

# Google Sheets authentication
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
credentials = ServiceAccountCredentials.from_json_keyfile_name("google_sheet_keys_aisyah.json", scope)
client = gspread.authorize(credentials)

# Open your Google Sheet
sheet = client.open("cat").sheet1  # Replace with your sheet name
data = sheet.get_all_records()

# Convert to DataFrame
df = pd.DataFrame(data)

# Show DataFrame in Streamlit
st.dataframe(df)

# Optional filtering
if st.checkbox("Filter by breed"):
    breed = st.selectbox("Choose a breed", df['Breed'].unique())
    st.write(df[df['Breed'] == breed])
