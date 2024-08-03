#!/bin/bash

# Define the Python script file name
PYTHON_SCRIPT="ping_urls.py"

# Check if the Python script exists
if [ ! -f "$PYTHON_SCRIPT" ]; then
  echo "Python script $PYTHON_SCRIPT not found!"
  exit 1
fi

# Run the Python script
python3 "$PYTHON_SCRIPT"

# Check if the Python script ran successfully
if [ $? -eq 0 ]; then
  echo "Python script executed successfully."
else
  echo "Python script failed to execute."
  exit 1
fi
