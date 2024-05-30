% scale(1000) import("/../meshes/urdf_palm_right.stl");

// Upper Part
translate([78, 0, -456]) {
    cube([20, 50, 30], center = true);
}

// Lower Part
translate([78, 10, -500]) {
    cube([20, 30, 50], center = true);
}