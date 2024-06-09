"""
This script inserts the OnShape api keys, set by the docker .env-file, into the config.json.
"""

import json
import os

# Path to the configuration file
CONFIG_FILE_PATH = 'onshape-to-robot_config_files/config.json'

# Read the JSON-file
with open(file=CONFIG_FILE_PATH, mode="r", encoding="utf-8") as jsonFile:
    config = json.load(jsonFile)

    # Update the access and secret keys with environment variables
    config['onshape_access_key'] = os.getenv('ONSHAPE_ACCESS_KEY')
    config['onshape_secret_key'] = os.getenv('ONSHAPE_SECRET_KEY')

with open(file=CONFIG_FILE_PATH, mode="w", encoding="utf-8") as jsonFile:
    json.dump(config, jsonFile)
