% scale(1000) import("/../meshes/urdf_palm_left.stl");

// Upper Part
translate([-157.5, 0, -101]) {
    cube([50, 20, 30], center = true);
}

// Lower Part
translate([-168, 00, -56]) {
    cube([30, 20, 50], center = true);
}