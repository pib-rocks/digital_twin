"""
This script creates a MJCF-file from the exported URDF-file.
"""

import os
from urdf2mjcf import convert

# File paths
INPUT_FILES_PATH = "/app/onshape-to-robot_input_files/"
URDF_WITH_MUJOCO_HEADER = INPUT_FILES_PATH + "mujoco_file_with_header.urdf"
CONVERTED_MJCF_FILE = INPUT_FILES_PATH + "pib.mjcf"

# Check if the URDF file exists in the current directory
if os.path.exists(URDF_WITH_MUJOCO_HEADER):
    try:
        # Convert URDF to MJCF
        convert.convert_urdf_to_mjcf(URDF_WITH_MUJOCO_HEADER, CONVERTED_MJCF_FILE)
        print(f"Conversion successful! MJCF file saved as: {CONVERTED_MJCF_FILE}")
    except Exception as e:
        print(f"Error during conversion: {e}")
else:
    print(f"Error: The file '{URDF_WITH_MUJOCO_HEADER}' does not exist in the current directory.")
