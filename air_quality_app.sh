#!/bin/bash

echo "🔄 Starting FastAPI backend in Docker..."
docker build -t air_quality_api . || { echo "❌ Docker build failed"; exit 1; }

# Stop existing container if needed
docker stop air_quality_api_container >/dev/null 2>&1
docker rm air_quality_api_container >/dev/null 2>&1

# Run container in background
docker run -d -p 8005:8005 --name air_quality_api_container air_quality_api

sleep 3

echo "🚀 Launching Streamlit frontend..."
# Activate your conda/venv if needed here
streamlit run src/streamlit_app.py