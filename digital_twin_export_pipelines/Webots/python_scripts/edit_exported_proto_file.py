"""
This script prepares the exported URDF file to be used in Webots.
"""

import xml.etree.ElementTree as ET


def edit_proto(target_proto_path):
    """Fix indentations and unnecessary empty lines"""

    # Read out the .proto file content
    with open(target_proto_path, "r") as target_file:
        modified_file_content = target_file.read()

    # Change the name of the PROTO node to 'pib'
    modified_file_content = modified_file_content.replace("PROTO webots", "PROTO Pib")

    # Change the name of the Robot.name attribute
    modified_file_content = modified_file_content.replace(
        'name            "webots"', 'name            "pib"'
    )

    # Change the maxTorque from 1.0 to 10.0
    modified_file_content = modified_file_content.replace(
        "maxTorque 1.0", "maxTorque 10.0"
    )

    # Replace directory path to the mesh files
    # For some reason only the last 25 letters of the 'onshape-to-robot_config_files' file path are appended by urdf2webots
    modified_file_content = modified_file_content.replace(
        "ape-to-robot_config_files/package:/pibsim_webots/",
        "/home/pib/ros_working_dir/src/pibsim_webots/protos/meshes/",
    )

    # Replace the info at the beginning of the file
    modified_file_content = modified_file_content.replace(
        "This is a proto file for Webots for the webots",
        "This is a proto file for Webots for the humanoid robot pib",
    )

    with open(target_proto_path, "w") as target_file:
        target_file.write(modified_file_content)


# File paths
TARGET_PROTO_PATH = "onshape-to-robot_config_files/webots.proto"

edit_proto(TARGET_PROTO_PATH)
