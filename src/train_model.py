import os
import joblib

import pandas as pd
import numpy as np 

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
# from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
from xgboost import XGBClassifier

from imblearn.over_sampling import SMOTE

# Loading in the data
df = pd.read_csv("data/processed/pm25_labeled.csv")

# Data cleaning...
df = df[df["pm25"] > 0 ] # drop invalid
df["datetime_utc"] = pd.to_datetime(df["datetime_utc"]) # format datetime
df["hour"] = df["datetime_utc"].dt.hour # Create hour instance
df["month"] = df["datetime_utc"].dt.month # Create month instance

# Labelling...
l = LabelEncoder()
df["training_label"] = l.fit_transform(df["air_quality"])

# Feature selection...
cols = ["pm25", "latitude", "longitude", "hour", "month"]

# Training... 
x = df[cols]
y = df["training_label"]
x_train, x_test, y_train, y_test = train_test_split(x, y, stratify=y, test_size=0.2, random_state=42)

x_train = x_train.dropna()
y_train = y_train.loc[x_train.index]

scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.fit_transform(x_test)

smote= SMOTE(random_state = 42)
x_train_resampled, y_train_resampled = smote.fit_resample(x_train_scaled, y_train)

xgb_model = XGBClassifier(use_label_encoder= False, eval_metric = 'mlogloss', random_state= 42)
xgb_model.fit(x_train_resampled, y_train_resampled)

# Evaluation...
y_prediction = xgb_model.predict(x_test_scaled)
print(f"Eval.: {classification_report(y_test, y_prediction)}")
print(f"Confusion matrix: {confusion_matrix(y_test, y_prediction)}")

os.makedirs("models", exist_ok=True)
joblib.dump(xgb_model, "models/xgb_model.pkl")
joblib.dump(scaler, "models/skaler.pkl")
joblib.dump(l, "models/label_encoder.pkl")

print("success")


# FOREST MODEL
# forest_model = RandomForestClassifier(n_estimators=100, class_weight="balanced", random_state=42)
# forest_model.fit(x_train_resampled, y_train_resampled)

# # Evaulation...
# y_prediction = forest_model.predict(x_test_scaled)
# print(f"Eval.: {classification_report(y_test, y_prediction)}")
# print(f"Confusion matrix: {confusion_matrix(y_test, y_prediction)}")

# os.makedirs("models", exist_ok = True)
 # joblib.dump(forest_model, "models/forest_model.pkl")