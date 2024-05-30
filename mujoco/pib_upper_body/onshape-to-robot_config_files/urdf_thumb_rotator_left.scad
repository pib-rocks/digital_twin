% scale(1000) import("/../meshes/urdf_thumb_rotator_left.stl");

translate([88,-28,-510]) {
    rotate([-12, 0, 0]) {
        cylinder(34, 5, 8, center = false);
    }
}