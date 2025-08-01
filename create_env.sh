#!/bin/bash

# Exit on error
set -e

# Define the environment name
ENV_NAME=".venv"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"

echo "Creating Python virtual environment: $ENV_NAME"
python3 -m venv "$SCRIPT_DIR/$ENV_NAME"

# Activate the virtual environment
source "$SCRIPT_DIR/$ENV_NAME/bin/activate"

echo "Installing required dependencies..."
pip install --upgrade pip
pip install loguru==0.7.2 pygame==2.6.1

echo "Environment setup complete. You can activate it with:"
echo "source $SCRIPT_DIR/$ENV_NAME/bin/activate"
