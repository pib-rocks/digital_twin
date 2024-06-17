% scale(1000) import("/../meshes/urdf_finger_distal.stl");

translate([75,-51,-639.5]) {
    rotate([-10, 0, 0]) {
        cylinder(h=45, r=8, center = false);
    }
}