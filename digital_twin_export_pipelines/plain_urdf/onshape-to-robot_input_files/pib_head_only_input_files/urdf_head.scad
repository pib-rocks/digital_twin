% scale(1000) import("/../meshes/urdf_head.stl");

// Document offsets
width_offset=-115;
depth_offset=-145;
height_offset=-68;

// Document dimensions
full_width=230;
full_depth=170;
full_height=200;

union() {
    // Front Cover
    front_cover_depth=155;
    
    translate([
    width_offset, 
    depth_offset + front_cover_depth, 
    height_offset]) {
        cube([
            full_width, 
            full_depth - front_cover_depth, 
            full_height], center = false);
    };
    

    // Head Plate Variables
    head_depth=27;
    head_height=68;
    head_plate_thickness=25;
    
    // Left Head Plate
    translate([
    width_offset,
    depth_offset + head_depth,
    height_offset + head_height]) {
        cube([
            head_plate_thickness, 
            full_depth - head_depth, 
            full_height - head_height], 
            center = false);
    }

    // Right Head Plate
    translate([
    width_offset + full_width - head_plate_thickness,
    depth_offset + head_depth,
    height_offset + head_height]) {
        cube([
            head_plate_thickness, 
            full_depth - head_depth, 
            full_height - head_height], 
            center = false);
    }
    
    // Upper Head Plate
    translate([
    width_offset,
    depth_offset + head_depth,
    height_offset + full_height - head_plate_thickness]) {
        cube([
            full_width, 
            full_depth - head_depth, 
            head_plate_thickness], 
            center = false);
    }
}