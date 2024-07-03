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


def apply_xml_formatting(target_xml_path):
    """Fix indentations and unnecessary empty lines"""

    # Parse the source XML and get the root element
    source_xml_tree = ET.parse(target_xml_path)
    root = source_xml_tree.getroot()

    # Apply indentation formatting to the entire XML for better readability
    ET.indent(root)

    # Overwrite the original unformatted file
    source_xml_tree.write(target_xml_path)


# File paths
MUJOCO_HEADER_XML_PATH = "python_scripts/mujoco_header.xml"
TARGET_XML_PATH = "onshape-to-robot_config_files/robot.urdf"
OUTPUT_XML_PATH = "onshape-to-robot_config_files/mujoco.urdf"

insert_element(MUJOCO_HEADER_XML_PATH, TARGET_XML_PATH, OUTPUT_XML_PATH)
apply_xml_formatting(OUTPUT_XML_PATH)
