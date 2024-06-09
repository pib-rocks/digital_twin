#!/bin/bash

# Exit immediately if any command returns a non-successful exit status
set -e

# Run all python scripts nececcary for the onshape export
python ./python_scripts/prepare_config_file_for_export.py
python ./python_scripts/generate_mujoco_digital_twin.py