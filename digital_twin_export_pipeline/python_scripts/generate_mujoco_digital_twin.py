"""
This script creates a MuJoCo-compatible URDF-file from the pib onshape .stl files.
"""

import subprocess

# Run the onshape-to-robot export
result = subprocess.run(
    ["onshape-to-robot", "/app/onshape-to-robot_config_files"],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    check=True
)
