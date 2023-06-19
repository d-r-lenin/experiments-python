#!/bin/bash

cd ..

# Create a virtual environment
python3 -m venv env

# Activate the virtual environment
. env/bin/activate

# Install dependencies
pip install -r requirements.txt

# deactivate the virtual environment
deactivate
