"""
This script moves all relevant files into the exchange directory.
"""

import os
import shutil

# Path variables
EXPORT_DIR = "/app/onshape-to-robot_input_files"
MOUNTED_EXCHANGE_DIR = "/app/export"

# Loop through all files in the export directory
files = os.listdir(EXPORT_DIR)

for file in files:
    shutil.move(os.path.join(EXPORT_DIR, file), MOUNTED_EXCHANGE_DIR)
