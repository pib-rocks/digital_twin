"""
This script creates a MJCF-file from a URDF-file.
"""

import os
from urdf2mjcf import convert

# File paths
INPUT_FILES_PATH = "/app/onshape-to-robot_input_files/"
ABSOLUTE_PATH_URDF = INPUT_FILES_PATH + "absolute_path.urdf"
CONVERTED_MJCF_FILE = INPUT_FILES_PATH + "pib.mjcf"

# Check if the URDF file exists in the current directory
if os.path.exists(ABSOLUTE_PATH_URDF):
    try:
        # Convert URDF to MJCF
        convert.convert_urdf_to_mjcf(ABSOLUTE_PATH_URDF, CONVERTED_MJCF_FILE)
        print(f"Conversion successful! MJCF file saved as: {CONVERTED_MJCF_FILE}")
    except Exception as e:
        print(f"Error during conversion: {e}")
else:
    print(f"Error: The file '{ABSOLUTE_PATH_URDF}' does not exist in the current directory.")
