import streamlit as st
import requests

st.title("Air Quality Predictor")
st.markdown("Enter values below to get a prediction from the API.")

# inputs
pm25 = st.number_input("PM2.5 Value", min_value=0.0, step=0.1, value=15.0)
latitude = st.number_input("Latitude", value=37.7749)
longitude = st.number_input("Longitude", value=-122.4194)
hour = st.number_input("Hour of Day (0-23)", min_value=0, max_value=23, value=14)
month = st.number_input("Month (1-12)", min_value=1, max_value=12, value=6)

# predict btn
if st.button("Predict Air Quality"):
    payload = {
        "pm25": pm25,
        "latitude": latitude,
        "longitude": longitude,
        "hour": hour,
        "month": month
    }

    try:
        response = requests.post("http://127.0.0.1:8005/predict", json=payload)
        if response.status_code == 200:
            result = response.json()
            st.success(f"🌍 Predicted Air Quality: **{result['prediction']}**")
        else:
            st.error(f"Error: {response.status_code} - {response.text}")
    except Exception as e:
        st.error(f"Could not connect to API: {e}")