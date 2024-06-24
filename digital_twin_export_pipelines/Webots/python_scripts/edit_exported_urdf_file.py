"""
This script prepares the exported URDF file to be used in Webots.
"""

import xml.etree.ElementTree as ET


def apply_xml_formatting(target_xml_path):
    """Fix indentations and unnecessary empty lines"""

    # Parse the source XML and get the root element
    source_xml_tree = ET.parse(target_xml_path)
    root = source_xml_tree.getroot()

    # Apply indentation formatting to the entire XML for better readability
    ET.indent(root)

    # Overwrite the original unformatted file
    source_xml_tree.write(OUTPUT_XML_PATH)


# File paths
TARGET_XML_PATH = "onshape-to-robot_config_files/robot.urdf"
OUTPUT_XML_PATH = "onshape-to-robot_config_files/webots.urdf"

apply_xml_formatting(TARGET_XML_PATH)
