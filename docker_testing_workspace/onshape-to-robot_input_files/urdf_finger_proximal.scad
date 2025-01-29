% scale(1000) import("/../meshes/urdf_finger_proximal.stl");

translate([79,-41,-586]) {
    rotate([-10, 0, 0]) {
        cylinder(h=38, r=9, center = false);
    }
}