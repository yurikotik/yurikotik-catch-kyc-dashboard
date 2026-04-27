import streamlit as st
from supabase import create_client, Client

# --- Supabase connection ---
url = "https://asnyvuksnlhvqajrtrrr.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImFzbnl2dWtzbmxodnFhanJ0cnJyIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzczMDI4MzcsImV4cCI6MjA5Mjg3ODgzN30.xH4yGSJssOfas5_G4-0G3lrFYZ57G4biTvguquzp250"

supabase: Client = create_client(url, key)

st.title("Catch-KYC Dashboard — Live Top 20 Data")

# --- Fetch data ---
response = supabase.table("top20").select("*").execute()
rows = response.data

if not rows:
    st.warning("No data found in Supabase table.")
else:
    st.success("Live data loaded from Supabase.")
    st.dataframe(rows)

