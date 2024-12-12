#!/bin/bash
rasa run --enable-api --port 5005 &  # Start Rasa in the background
python app.py  # Start Flask
