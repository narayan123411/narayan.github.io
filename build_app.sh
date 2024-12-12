#!/bin/bash

pip install -r requirements.txt
echo "Training rasa model"
rasa train
echo "rasa model trained successfully!"
