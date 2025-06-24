import sys
import joblib
import numpy as np
import os

model = joblib.load("models/forest_model.pkl")
scaler = joblib.load("models/skaler.pkl")
encoder = joblib.load("models/label_encoder.pkl")

#input check
if len(sys.argv) != 6:
    print("Usage: python predict_cli.py pm25 latitude longitude hour month")
    sys.exit(1)

pm25 = float(sys.argv[1])
latitude = float(sys.argv[2])
longitude = float(sys.argv[3])
hour = int(sys.argv[4])
month = int(sys.argv[5])

# scale inputs
features = np.array([[pm25, latitude, longitude, hour, month]])
features_scaled = scaler.transform(features)

# Finally, predict!!!
prediction = model.predict(features_scaled)
label = encoder.inverse_transform(prediction)[0]

#Check this label
print(f"Air quality prediction: {label}")