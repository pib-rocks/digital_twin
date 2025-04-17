"""
This script moves all .stl files into a separate folder.
"""

import os
import shutil

# Path variables
ONSHAPE_TO_ROBOT_DIR = "onshape-to-robot_input_files/"
ASSETS_DIR = ONSHAPE_TO_ROBOT_DIR + "assets"

# Create the meshes folder depending on weather or not it exists
MESHES_DIR = os.path.join(ONSHAPE_TO_ROBOT_DIR, "meshes")
DIRECTORY_EXISTS = os.path.exists(MESHES_DIR)
if not DIRECTORY_EXISTS:
    os.makedirs(MESHES_DIR)

# Loop through all files in the export directory
files = os.listdir(ASSETS_DIR)

for file in files:
    # Move all .stl-files to the meshes directory
    if file.endswith(".stl"):
        shutil.move(os.path.join(ASSETS_DIR, file), MESHES_DIR)
