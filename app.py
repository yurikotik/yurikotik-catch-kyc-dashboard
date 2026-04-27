from supabase import create_client
import streamlit as st

url = "https://asnyvuksnlhvqajrtrrr.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImFzbnl2dWtzbmxodnFhanJ0cnJyIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzczMDI4MzcsImV4cCI6MjA5Mjg3ODgzN30.xH4yGSJssOfas5_G4-0G3lrFYZ57G4biTvguquzp250"

supabase = create_client(url, key)

