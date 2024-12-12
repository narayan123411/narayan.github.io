#!/bin/bash

# Start Rasa in the background
rasa run --host 0.0.0.0 --port 5005 &

# Run your app (optional, if necessary)
python app.py

# Keep the container running
wait
