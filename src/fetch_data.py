import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")

if not API_KEY:
    raise ValueError("API key not found... ")

# parameter_id = 2
url = "https://api.openaq.org/v3/parameters/2/latest?limit=1000"
headers = {"x-api-key": API_KEY}

response = requests.get(url, headers=headers)
data = response.json()

os.makedirs("data/raw", exist_ok=True)
output_path = "data/raw/raw_data_GBpm25.json"
with open(output_path, "w") as f:
    json.dump(data, f, indent=2)

print(f"Saved data to: {output_path}")