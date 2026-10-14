import joblib
import numpy as np
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Load the trained model and label encoder
model = joblib.load("crop_recommendation_model.pkl")
le = joblib.load("label_encoder.pkl")


class CropInput(BaseModel):
  N: float
  P: float
  K: float
  temperature: float
  humidity: float
  ph: float
  rainfall: float


@app.get("/")
def home():
  return {"message": "Crop Recommendation ML Backend is running!"}


@app.post("/predict")
def predict(data: CropInput):
  user_data = pd.DataFrame([{
      "N": data.N,
      "P": data.P,
      "K": data.K,
      "temperature": data.temperature,
      "humidity": data.humidity,
      "ph": data.ph,
      "rainfall": data.rainfall,
  }])

  # Predict top 3 crops using probabilities
  probs = model.predict_proba(user_data)
  top_3_idx = np.argsort(probs, axis=1)[:, -3:][:, ::-1]
  top_3_crops = le.inverse_transform(top_3_idx[0])

  return {
      "best_crop": str(top_3_crops[0]),
      "second_best": str(top_3_crops[1]),
      "third_best": str(top_3_crops[2]),
  }