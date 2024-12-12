#!/bin/bash

pip install -r requirements.txt
echo "Training rasa model"
rasa clean
rasa train --debug
echo "rasa model trained successfully!"
