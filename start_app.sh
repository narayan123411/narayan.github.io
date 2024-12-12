#!/bin/bash

echo "Starting Rasa server..."
rasa run --enable-api --port 5005 &  # Start Rasa in the background
RASA_PID=$!
echo "Rasa server started in the background, PID: $RASA_PID"

# Wait for Rasa to be ready
echo "Waiting for Rasa to be ready..."
sleep 5  # Give Rasa some time to start, or you can use a better check for readiness

echo "Starting Flask app..."
gunicorn app:app  # Start Flask

# Run your app (optional, if necessary)
echo "Starting python..."
python app.py

# Keep the container running
wait

echo "Flask app started"
