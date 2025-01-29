#!/bin/bash

# Exit immediately if any command returns a non-successful exit status
set -e

# Function to print the current timestamp and a message
print_timestamp() {
    echo "$(date '+%Y-%m-%d %H:%M:%S') - $1"
}

# Run python scripts
print_timestamp "Setting environment variables"
python /app/python_scripts/01_prepare_config_file_for_export.py

print_timestamp "Preparing config file"
python /app/python_scripts/02_export_urdf_from_onshape.py