% scale(1000) import("/../meshes/urdf_thumb_rotator_right.stl");

translate([-202,29,-210]) {
    rotate([12, 0, 0]) {
        cylinder(34, 5, 8, center = false);
    }
}