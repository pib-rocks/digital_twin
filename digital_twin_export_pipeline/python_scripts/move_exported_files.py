"""
This script moves all .stl files into a new folder.
"""

import os
import shutil

# Create a directory named "meshes" in the export directory
EXPORT_DIR = "onshape-to-robot_config_files/"
MESHES_DIR = os.path.join(EXPORT_DIR, "meshes")
os.makedirs(MESHES_DIR)

# Loop through all files in the export directory
files = os.listdir(EXPORT_DIR)

for file in files:
    # Move all .stl-files to the meshes directory
    if file.endswith(".stl"):
        shutil.move(os.path.join(EXPORT_DIR, file), MESHES_DIR)
