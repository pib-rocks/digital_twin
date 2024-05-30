% scale(1000) import("/../meshes/urdf_finger_proximal.stl");

// Document offsets
full_width_offset=-55.2;
full_depth_offset=-155;
full_height_offset=-47;

// Document dimensions
full_width=110;
full_depth=93;
full_height=30;

translate([
    full_width_offset, 
    full_depth_offset, 
    full_height_offset]) {
        cube([
            full_width, 
            full_depth, 
            full_height], 
            center = false);
}