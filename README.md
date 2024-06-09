# Digital Twin for pib

## How to start the export
1. Create a file called ".env" in the "digital_twin_export_pipeline" folder
2. Fill in your OnShape api keys (as shown in the example)
3. Fill in the name of the input_files folder you want to export (as shown in the example)
4. Open a terminal in the "digital_twin_export_pipeline" folder
5. Run this command to start the export: `docker-compose up`
6. Run this command to extract the exported files from the docker volume:  
   `docker cp digital-twin-container:/app/onshape-to-robot_config_files ./Exported_Digital_Twin`

## Environment file for docker

## Structure of .env:
```
ONSHAPE_ACCESS_KEY=enter_your_access_key_here
ONSHAPE_SECRET_KEY=enter_your_secret_key_here
INPUT_FILES_DIRECTORY=enter_the_folder_path_here
```

## Example for .env:
``` 
# Onshape API-Keys from onshape developer page
ONSHAPE_ACCESS_KEY=abcdefghijklmn0123456789
ONSHAPE_SECRET_KEY=abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKL

# The directory containing the config.json and the optional .scad files for onshape-to-robot
INPUT_FILES_DIRECTORY=pib_upper_body_input_files/pib_upper_body_export_files
```