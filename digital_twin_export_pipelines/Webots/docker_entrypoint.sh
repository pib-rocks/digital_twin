#!/bin/bash

# Exit immediately if any command returns a non-successful exit status
set -e

# Function to print the current timestamp and a message
print_timestamp() {
    echo "$(date '+%Y-%m-%d %H:%M:%S') - $1"
}

# Run all python scripts nececcary for the onshape export
print_timestamp "Preparing config file"
python ./python_scripts/prepare_config_file_for_export.py

print_timestamp "Exporting digital twin, this might take a few minutes."
python ./python_scripts/generate_webots_digital_twin.py

print_timestamp "Edit and format URDF file"
python ./python_scripts/edit_exported_proto_file.py

print_timestamp "Move all files to export directory"
python ./python_scripts/move_exported_files.py
