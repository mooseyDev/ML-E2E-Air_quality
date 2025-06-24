# ML-E2E-Air_quality
A full stack demo of ML workflow on air quality public data. 

Specifically, An end-to-end machine learning project that pulls open air quality data from the OpenAQ API, trains a model, and deploys it via FastAPI and Streamlit.

## Goals
- To practice full ML pipeline: ingest → clean → train → evaluate → deploy in preperation for larger project
- Predict air quality category from pollution for fun
- Understand how to serve models via REST API and frontend
- To understand and employ version control with Git/GitHub

## Stack
- Python3
- pandas, numpy, scikit-learn, matplotlib/seaborne
- FastAPI & Streamlit
- cURL for testing also
- Docker (for final packaging)

## To run
The app can be run from the cli using src/air_quality_predict.py

Example input: 
python src/air_quality_predict.py 15.0 37.77 -122.4 14 6

Example output: 
Air quality prediction: Poor

## Ignore
UserWarning: X does not have valid feature names, but StandardScaler was fitted with feature names
  warnings.warn
