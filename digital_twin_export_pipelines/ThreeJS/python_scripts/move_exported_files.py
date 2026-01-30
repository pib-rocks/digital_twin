"""
This script moves all .stl files into a new folder.
"""

import os
import shutil

# Path variables
ONSHAPE_TO_ROBOT_DIR = "onshape-to-robot_config_files/"
MOUNTED_EXCHANGE_DIR = "/app/export"

# Loop through all files in the export directory
files = os.listdir(ONSHAPE_TO_ROBOT_DIR)

for file in files:
    # Move all .stl-files to the specified directory
    if file.endswith(".stl"):
        shutil.move(os.path.join(ONSHAPE_TO_ROBOT_DIR, file), MOUNTED_EXCHANGE_DIR)

# Move relevant files to exchange directory
shutil.move(os.path.join(ONSHAPE_TO_ROBOT_DIR, "robot.urdf"), MOUNTED_EXCHANGE_DIR)
