"""
This script creates a MJCF-file from a URDF-file.
"""

import os
from urdf2mjcf import convert

# Define the URDF file and MJCF output file names
folder_path="/app/onshape-to-robot_input_files/"
urdf_filename = folder_path + "robot.urdf"
mjcf_filename = folder_path + "conv.mjcf"

# Check if the URDF file exists in the current directory
if os.path.exists(urdf_filename):
    try:
        # Convert URDF to MJCF
        convert.convert_urdf_to_mjcf(urdf_filename, mjcf_filename)
        print(f"Conversion successful! MJCF file saved as: {mjcf_filename}")
    except Exception as e:
        print(f"Error during conversion: {e}")
else:
    print(f"Error: The file '{urdf_filename}' does not exist in the current directory.")
