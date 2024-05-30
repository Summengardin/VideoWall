#!/bin/bash

# Install python venv
if [ ! -d "venv" ]; then
    sudo apt install -y python3-venv
    python3 -m venv venv
fi

# Activate python venv
source venv/bin/activate

