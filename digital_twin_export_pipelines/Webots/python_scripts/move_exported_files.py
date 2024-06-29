"""
This script moves all .stl files into a new folder.
"""

import os
import shutil

# Path variables
ONSHAPE_TO_ROBOT_DIR = "onshape-to-robot_config_files/"
MOUNTED_EXCHANGE_DIR = "/app/export"

# Create a directory named "meshes" in the export directory
MESHES_DIR = os.path.join(ONSHAPE_TO_ROBOT_DIR, "meshes")
os.makedirs(MESHES_DIR)

# Loop through all files in the export directory
files = os.listdir(ONSHAPE_TO_ROBOT_DIR)

for file in files:
    # Move all .stl-files to the meshes directory
    if file.endswith(".stl"):
        shutil.move(os.path.join(ONSHAPE_TO_ROBOT_DIR, file), MESHES_DIR)

# Move relevant files to exchange directory
shutil.move(MESHES_DIR, MOUNTED_EXCHANGE_DIR)
shutil.move(os.path.join(ONSHAPE_TO_ROBOT_DIR, "webots.urdf"), MOUNTED_EXCHANGE_DIR)
shutil.move(os.path.join(ONSHAPE_TO_ROBOT_DIR, "webots.proto"), MOUNTED_EXCHANGE_DIR)
