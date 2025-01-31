"""
This script prepares the exported URDF file to be used in MuJoCo.
"""

import xml.etree.ElementTree as ET
import os

def insert_element(source_xml_path, target_xml_path, output_xml_path):
    """Add the MuJoCo XML element of the source file to the robot element of the target file."""

    # Parse the source XML to get the MuJoCo element
    source_tree = ET.parse(source_xml_path)
    mujoco_element = source_tree.getroot()

    # Parse the target XML to insert the element
    target_tree = ET.parse(target_xml_path)
    robot_element = target_tree.getroot()

    # Insert the MuJoCo element as the first child of the <robot> element
    # robot_element.insert(0, mujoco_element)

    # Save the result as new file
    target_tree.write(output_xml_path)


def convert_relative_to_absolute(urdf_path, output_path, base_path):
    """Replace relative mesh filepaths with absolute paths."""
    # Parse the XML file
    tree = ET.parse(urdf_path)
    root = tree.getroot()

    # Find all mesh elements and update the filename
    for mesh in root.findall(".//mesh"):
        filename = mesh.get("filename")
        if filename and filename.startswith("package:///"):
            # Extract just the filename
            mesh_filename = os.path.basename(filename)
            # Construct the new absolute path
            new_path = os.path.join(base_path, "meshes", mesh_filename)
            mesh.set("filename", new_path)

    # Save the modified URDF
    tree.write(output_path, encoding="utf-8", xml_declaration=True)



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
INPUT_FILES_PATH = "/app/onshape-to-robot_input_files/"
MUJOCO_HEADER_XML_PATH = "/app/python_scripts/mujoco_header.xml"
ONSHAPE_EXPORT_URDF = INPUT_FILES_PATH + "robot.urdf"
URDF_WITH_MUJOCO_HEADER = INPUT_FILES_PATH + "mujoco_header.urdf"
ABSOLUTE_PATH_URDF = INPUT_FILES_PATH + "absolute_path.urdf"

#insert_element(MUJOCO_HEADER_XML_PATH, ONSHAPE_EXPORT_URDF, URDF_WITH_MUJOCO_HEADER)
convert_relative_to_absolute(ONSHAPE_EXPORT_URDF, ABSOLUTE_PATH_URDF, INPUT_FILES_PATH)


apply_xml_formatting(ABSOLUTE_PATH_URDF)
