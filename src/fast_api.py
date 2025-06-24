from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

model =joblib.load("models/xgb_model.pkl")
scaler= joblib.load("models/skaler.pkl")
label_encoder = joblib.load('models/label_encoder.pkl')

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Runing"}

class InputFeatures(BaseModel):
    pm25: float
    latitude: float
    longitude: float
    hour: int
    month: int

@app.post("/predict")
def predict_air_quality(features: InputFeatures):
    input_data = np.array([[
        features.pm25,
        features.latitude,
        features.longitude,
        features.hour,
        features.month
    ]])

    # Scale input
    scaled = scaler.transform(input_data)
    
    # Make prediction
    prediction = model.predict(scaled)
    label = label_encoder.inverse_transform([prediction])[0]
    
    return {
        "prediction": label,
        "input": features.dict()
    }