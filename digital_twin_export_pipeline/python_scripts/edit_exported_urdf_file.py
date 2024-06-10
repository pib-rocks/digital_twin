"""
This script prepares the exported URDF file to be used in MuJoCo.
"""

import xml.etree.ElementTree as ET

def insert_element(source_xml_path, target_xml_path, output_xml_path):
    """Add the MuJoCo XML element of the source file to the robot element of the target file."""

    # Parse the source XML to get the MuJoCo element
    source_tree = ET.parse(source_xml_path)
    mujoco_element = source_tree.getroot()

    # Parse the target XML to insert the element
    target_tree = ET.parse(target_xml_path)
    robot_element = target_tree.getroot()

    # Insert the MuJoCo element as the first child of the <robot> element
    robot_element.insert(0, mujoco_element)

    # Save the result as new file
    target_tree.write(output_xml_path)

# File paths
MUJOCO_HEADER_XML_PATH = "python_scripts/mujoco_header.xml"
TARGET_XML_PATH = "onshape-to-robot_config_files/robot.urdf"
OUTPUT_XML_PATH = "onshape-to-robot_config_files/mujoco.urdf"

insert_element(MUJOCO_HEADER_XML_PATH, TARGET_XML_PATH, OUTPUT_XML_PATH)
