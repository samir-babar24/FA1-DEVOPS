import requests
import streamlit as st

st.title("🌾 Smart Crop Recommendation System")
st.write(
    "Enter your soil and climate conditions to find the best crops to grow!"
)

# Input fields for the 7 features
col1, col2 = st.columns(2)

with col1:
  N = st.number_input("Nitrogen (N)", min_value=0.0, max_value=200.0, value=50.0)
  P = st.number_input(
      "Phosphorus (P)", min_value=0.0, max_value=200.0, value=50.0
  )
  K = st.number_input("Potassium (K)", min_value=0.0, max_value=200.0, value=50.0)
  temperature = st.number_input(
      "Temperature (°C)", min_value=0.0, max_value=60.0, value=25.0
  )

with col2:
  humidity = st.number_input(
      "Humidity (%)", min_value=0.0, max_value=100.0, value=60.0
  )
  ph = st.number_input("Soil pH", min_value=0.0, max_value=14.0, value=6.5)
  rainfall = st.number_input(
      "Rainfall (mm)", min_value=0.0, max_value=500.0, value=100.0
  )

if st.button("Get Crop Recommendations"):
  payload = {
      "N": N,
      "P": P,
      "K": K,
      "temperature": temperature,
      "humidity": humidity,
      "ph": ph,
      "rainfall": rainfall,
  }

  try:
    # Sends data to the backend container
    response = requests.post("http://localhost:8000/predict", json=payload)
    if response.status_code == 200:
      result = response.json()
      st.success("Analysis Complete!")
      st.markdown(f"### 🥇 Best Crop: **{result['best_crop']}**")
      st.markdown(f"### 🥈 Second Best: **{result['second_best']}**")
      st.markdown(f"### 🥉 Third Best: **{result['third_best']}**")
    else:
      st.error("Error communicating with the backend API.")
  except Exception as e:
    st.error(f"Could not connect to backend service: {e}")