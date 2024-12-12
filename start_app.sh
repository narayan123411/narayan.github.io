#!/bin/bash
rasa run --enable-api --port 5005 &  # Start Rasa in the background
gunicorn app:app  # Start Flask
