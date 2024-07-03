"""
This script moves all .stl files into a new folder.
"""

import os
import shutil

# Path variables
ONSHAPE_TO_ROBOT_DIR = "onshape-to-robot_config_files/"
MOUNTED_EXCHANGE_DIR = "/app/export"

# Create a directory for the .stl-files in the export directory
STL_DIR = os.path.join(ONSHAPE_TO_ROBOT_DIR, "resources")
os.makedirs(STL_DIR)

# Loop through all files in the export directory
files = os.listdir(ONSHAPE_TO_ROBOT_DIR)

for file in files:
    # Move all .stl-files to the corresponding directory
    if file.endswith(".stl"):
        shutil.move(os.path.join(ONSHAPE_TO_ROBOT_DIR, file), STL_DIR)

# Move relevant files to exchange directory
shutil.move(STL_DIR, MOUNTED_EXCHANGE_DIR)
shutil.move(os.path.join(ONSHAPE_TO_ROBOT_DIR, "pib.proto"), MOUNTED_EXCHANGE_DIR)
