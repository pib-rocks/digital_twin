% scale(1000) import("/../meshes/urdf_head_base.stl");

// Document offsets
full_width_offset=-55.2;
full_depth_offset=-155;
full_height_offset=-47;

// Document dimensions
full_width=110;
full_depth=93;
full_height=30;

// Reused part dimensions
arm_width=8;
arm_depth=65;
short_arm_depth_offset=7;

union() {
    
    // Left arm
    translate([
    full_width_offset, 
    full_depth_offset + short_arm_depth_offset, 
    full_height_offset]) {
        cube([
        arm_width, 
        arm_depth - short_arm_depth_offset, 
        full_height], 
        center = false);
    }
    
    // Middle arm
    translate([
    full_width_offset + 63, 
    full_depth_offset, 
    full_height_offset]) {
        cube([
        arm_width, 
        arm_depth, 
        full_height], 
        center = false);
    }
    
    // Left arm
    translate([
    full_width_offset + 102.4, 
    full_depth_offset + short_arm_depth_offset, 
    full_height_offset]) {
        cube([
        arm_width, 
        arm_depth - short_arm_depth_offset,
        full_height], 
        center = false);
    }
    
    // Connector middle part
    translate([
    full_width_offset, 
    -90, 
    full_height_offset]) {
        cube([
        full_width, 
        10, 
        full_height], 
        center = false);
    }
    
    // Connector outer part
    outer_connector_width_offset=15;
    
    translate([
    full_width_offset + outer_connector_width_offset, 
    -80, 
    full_height_offset]) {
        cube([
        full_width - outer_connector_width_offset * 2, 
        10, 
        full_height], 
        center = false);
    }

}