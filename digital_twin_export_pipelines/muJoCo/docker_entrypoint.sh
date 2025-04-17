#!/bin/bash

# Exit immediately if any command returns a non-successful exit status
set -e

# Function to print the current timestamp and a message
print_timestamp() {
    echo "$(date '+%Y-%m-%d %H:%M:%S') - $1"
}

# Run all python scripts nececcary for the onshape export
print_timestamp "Preparing config file"
python ./python_scripts/step_01_prepare_config_file_for_export.py

print_timestamp "Exporting digital twin, this might take a few minutes."
python ./python_scripts/step_02_export_urdf_from_onshape.py

print_timestamp "Edit and format URDF file"
python ./python_scripts/step_03_edit_exported_urdf_file.py

print_timestamp "Move all stl files to a separate directory"
python ./python_scripts/step_04_move_stl_files.py

print_timestamp "Convert the urdf file to the mjcf format"
python ./python_scripts/step_05_convert_urdf_to_mjcf.py

print_timestamp "Move all files to export directory"
python ./python_scripts/step_06_move_files_to_exchange_directory.py
