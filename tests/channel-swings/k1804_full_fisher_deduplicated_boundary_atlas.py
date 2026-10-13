#!/usr/bin/env python3
"""Deduplicate K1796's retained-box faces and corners exactly."""
import importlib.util
import json
from collections import defaultdict
from hashlib import sha256
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ARTIFACT = ROOT / "lab/process/k1804-full-fisher-deduplicated-boundary-atlas.json"
BASE = ROOT / "tests/channel-swings/k1796_full_fisher_retained_box_enclosure_bank.py"
spec = importlib.util.spec_from_file_location("k1796_for_k1804", BASE)
k = importlib.util.module_from_spec(spec)
spec.loader.exec_module(k)


def retained_boxes():
    terms, _ = k.projection_terms()
    stack = [(slab, cell, box, 0) for slab, cell, box in k.roots()]
    retained = []
    while stack:
        slab, cell, box, depth = stack.pop()
        lower, _ = k.bernstein_bound(terms, box)
        if lower > 0:
            continue
        if depth == k.MAX_DEPTH:
            retained.append((slab, cell, box))
            continue
        ta, tb, za, zb = box
        if depth % 2 == 0:
            middle = (ta + tb) / 2
            children = ((ta, middle, za, zb), (middle, tb, za, zb))
        else:
            middle = (za + zb) / 2
            children = ((ta, tb, za, middle), (ta, tb, middle, zb))
        stack.extend((slab, cell, child, depth + 1)
                     for child in reversed(children))
    return sorted(retained, key=lambda row: (row[0], *row[2]))


def atomic_faces(boxes):
    vertical, horizontal = defaultdict(list), defaultdict(list)
    for _, _, (ta, tb, za, zb) in boxes:
        vertical[ta].append((za, zb)); vertical[tb].append((za, zb))
        horizontal[za].append((ta, tb)); horizontal[zb].append((ta, tb))
    rows = []
    for orientation, groups in (("v", vertical), ("h", horizontal)):
        for fixed, intervals in groups.items():
            points = sorted({value for interval in intervals for value in interval})
            for lo, hi in zip(points, points[1:]):
                if lo == hi:
                    continue
                incidence = sum(a <= lo and hi <= b for a, b in intervals)
                if incidence:
                    rows.append((orientation, fixed, lo, hi, incidence))
    return sorted(rows, key=lambda row: (row[0], row[1], row[2], row[3]))


def compute():
    boxes = retained_boxes()
    faces = atomic_faces(boxes)
    corners = sorted({(t, z) for _, _, (ta, tb, za, zb) in boxes
                      for t in (ta, tb) for z in (za, zb)})
    exposed_faces = [row for row in faces if row[4] == 1]
    internal_faces = [row for row in faces if row[4] > 1]
    exposed_vertices = {(row[1], endpoint) if row[0] == "v" else (endpoint, row[1])
                        for row in exposed_faces for endpoint in (row[2], row[3])}
    rows = [f"B:{slab}:{cell}:" + ":".join(map(str, box))
            for slab, cell, box in boxes]
    rows += [f"F:{orientation}:{fixed}:{lo}:{hi}:{incidence}"
             for orientation, fixed, lo, hi, incidence in faces]
    rows += [f"C:{t}:{z}:{int((t, z) in exposed_vertices)}" for t, z in corners]
    return {
        "input_partition_digest": json.loads(k.ARTIFACT.read_text())["enclosure"]["partition_digest"],
        "retained_boxes": len(boxes),
        "by_slab": {str(slab): sum(row[0] == slab for row in boxes) for slab in (2, 3)},
        "box_local_face_incidences": 4 * len(boxes),
        "box_local_corner_incidences": 4 * len(boxes),
        "unique_atomic_faces": len(faces),
        "exposed_atomic_faces": len(exposed_faces),
        "shared_internal_atomic_faces": len(internal_faces),
        "maximum_face_incidence": max(row[4] for row in faces),
        "unique_corner_points": len(corners),
        "exposed_boundary_vertices": len(exposed_vertices),
        "internal_corner_points": len(set(corners) - exposed_vertices),
        "slab_two_union_rectangle": {
            "t": [str(min(row[2][0] for row in boxes if row[0] == 2)),
                  str(max(row[2][1] for row in boxes if row[0] == 2))],
            "z": [str(min(row[2][2] for row in boxes if row[0] == 2)),
                  str(max(row[2][3] for row in boxes if row[0] == 2))],
            "box_count": sum(row[0] == 2 for row in boxes),
        },
        "atlas_digest": sha256("\n".join(rows).encode()).hexdigest(),
    }


def validate(data, got=None):
    got = compute() if got is None else got
    cert = data["certificate"]
    return [
        ("schema", data["schema_version"] == "1.0"),
        ("claim", data["claim_id"] == "K1804"),
        ("input", data["inputs"] == ["K1796"]),
        ("exact atlas replay", cert == got),
        ("85 boxes", got["retained_boxes"] == 85),
        ("slab split", got["by_slab"] == {"2": 7, "3": 78}),
        ("deduplicated", got["unique_atomic_faces"] < got["box_local_face_incidences"]
         and got["unique_corner_points"] < got["box_local_corner_incidences"]),
        ("shared faces recognized", got["shared_internal_atomic_faces"] > 0),
        ("slab two rectangle", got["slab_two_union_rectangle"]["box_count"] == 7),
        ("obligations remain", not data["decision"]["all_exposed_faces_and_corners_certified"]),
        ("not global", not data["decision"]["global_optimizer_proved"]),
    ]


def main():
    got = compute()
    if not ARTIFACT.exists() or "--print" in __import__("sys").argv:
        print(json.dumps(got, indent=2))
        return
    checks = validate(json.loads(ARTIFACT.read_text()), got)
    for index, (label, ok) in enumerate(checks, 1):
        assert ok, label
        print(f"PASS {index:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__":
    main()
