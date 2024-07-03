"""
This script creates a Webots-compatible URDF-file from the pib onshape .stl files.
"""

import subprocess

MOUNTED_EXCHANGE_DIR = "/app/export"

# Run the onshape-to-robot export
try:
    result = subprocess.run(
        ["onshape-to-robot", "/app/onshape-to-robot_config_files"],
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    print(result.stdout)

except subprocess.CalledProcessError as e:
    print("An error occurred while trying to export the digital twin:")
    print(e.stderr)

# Run the urdf to proto conversion
try:
    result = subprocess.run(
        [
            "python3",
            "-m",
            "urdf2webots.importer",
            "--input=/app/onshape-to-robot_config_files/robot.urdf",
            "--output=/app/onshape-to-robot_config_files/pib.proto"
        ],
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    print(result.stdout)

except subprocess.CalledProcessError as e:
    print("An error occurred while trying to export the digital twin:")
    print(e.stderr)
