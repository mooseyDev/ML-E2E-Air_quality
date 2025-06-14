import os
import json
import pandas as pd

raw_path = "data/raw/raw_data_pm25.json"
with open(raw_path, "r") as f:
    raw_data = json.load(f)
 
records = raw_data.get("results", [])

parsed = []
for entry in records:
    try:
        row = {
            "datetime_utc": entry["datetime"]["utc"],
            "pm25": entry["value"],
            "latitude": entry["coordinates"]["latitude"],
            "longitude": entry["coordinates"]["longitude"]
        }
        parsed.append(row)
    except KeyError:
        continue  

df = pd.DataFrame(parsed)
df = df[(df["pm25"] > 0) & (df["pm25"] <500)] # Removing outliers


def classify_pm25(value):
    if value <= 12.0:
        return "Good"
    elif value <= 35.4:
        return "Moderate"
    else:
        return "Poor"

df["air_quality"] = df["pm25"].apply(classify_pm25)

os.makedirs("data/processed", exist_ok=True)
output_path = "data/processed/pm25_labeled.csv"
df.to_csv(output_path, index=False)

print(f"Cleaned data and saved to {output_path}")