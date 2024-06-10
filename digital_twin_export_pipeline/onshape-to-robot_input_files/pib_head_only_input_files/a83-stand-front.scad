% scale(1000) import("/../meshes/a83-stand-front.stl");
rotate([0, 0, 60]){
    translate([-25, -185, 0]) {
        cube([50, 140, 20], center = false);
    }
}