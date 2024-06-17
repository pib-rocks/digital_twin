% scale(1000) import("/../meshes/urdf_body.stl");

// Document offsets
full_width_offset=-160;
full_depth_offset=-114.5;
full_height_offset=-836;

// Document dimensions
full_width=320;
full_depth=208.8;
full_height=932;

// Neck
translate([0,0,51]) {
        cylinder(h=89, r=35, center = true);
}

// Upper Body
translate([
    full_width_offset + 6, 
    full_depth_offset + 6, 
    full_height_offset + 650]) {
        cube([
            full_width - 12, 
            full_depth - 12, 
            full_height - 740], 
            center = false);
}

// Lower Body
translate([
    full_width_offset + 26, 
    full_depth_offset + 18, 
    full_height_offset + 370]) {
        cube([
            full_width - 51, 
            full_depth - 31, 
            full_height - 658], 
            center = false);
}

// Stand
translate([
    full_width_offset + 26, 
    full_depth_offset + 44, 
    full_height_offset]) {
        cube([
            full_width - 51, 
            full_depth - 82, 
            full_height - 618], 
            center = false);
}