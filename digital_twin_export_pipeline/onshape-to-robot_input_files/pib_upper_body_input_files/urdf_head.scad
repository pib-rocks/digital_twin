% scale(1000) import("/../meshes/urdf_head.stl");

// Document offsets
full_width_offset=-115;
full_depth_offset=-98;
full_height_offset=65;

// Document dimensions
full_width=230;
full_depth=170;
full_height=200;

// Variables
back_plate_depth_offset = full_depth_offset + 19;
back_plate_depth = 151;

// Front Head Plate
translate([
    full_width_offset, 
    full_depth_offset, 
    full_height_offset]) {
        cube([
            full_width, 
            18, 
            full_height], 
            center = false);
};

// Left Head Plate
translate([
    full_width_offset, 
    back_plate_depth_offset, 
    full_height_offset + 70]) {
        cube([
            25, 
            back_plate_depth, 
            130], 
            center = false);
}

// Right Head Plate
translate([
    full_width_offset + full_width - 25, 
    back_plate_depth_offset, 
    full_height_offset + 70]) {
        cube([
            25, 
            back_plate_depth, 
            130], 
            center = false);
}

// Top Head Plate
translate([
    full_width_offset + 26, 
    back_plate_depth_offset, 
    full_height_offset + 175]) {
        cube([
            full_width - (2*26), 
            back_plate_depth, 
            25], 
            center = false);
}