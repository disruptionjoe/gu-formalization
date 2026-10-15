#!/usr/bin/env python3
"""K1819: preserve the exposed slab-three boundary obligations."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ARTIFACT = ROOT / "lab/process/k1819-full-fisher-slab-three-boundary-cover.json"


def load(name):
    return json.loads((ROOT / f"lab/process/{name}.json").read_text())


def compute():
    atlas = load("k1804-full-fisher-deduplicated-boundary-atlas")
    cover = load("k1818-full-fisher-slab-three-stationary-cover")
    certificate = cover["certificate"]
    all_leaf_ids = list(range(atlas["certificate"]["by_slab"]["3"]))
    value_certified = [
        leaf_id for leaf_id in all_leaf_ids
        if leaf_id not in certificate["candidate_leaf_ids"]
    ]
    return {
        "input_partition_digest": atlas["certificate"]["input_partition_digest"],
        "retained_slab_three_leaves": atlas["certificate"]["by_slab"]["3"],
        "compact_value_certified_leaf_ids": value_certified,
        "whole_line_stationary_rejected_leaf_ids": certificate["stationary_rejected_leaf_ids"],
        "whole_line_stationary_retained_leaf_ids": certificate["stationary_retained_leaf_ids"],
        "exposed_atomic_faces": atlas["certificate"]["exposed_atomic_faces"],
        "exposed_boundary_vertices": atlas["certificate"]["exposed_boundary_vertices"],
        "certified_exposed_atomic_faces": 0,
        "certified_exposed_boundary_vertices": 0,
    }


def validate(data, got=None):
    got = compute() if got is None else got
    return [
        ("schema", data["schema_version"] == "1.0"),
        ("claim", data["claim_id"] == "K1819"),
        ("exact replay", data["certificate"] == got),
        ("78 leaves", got["retained_slab_three_leaves"] == 78),
        ("boundary census", got["exposed_atomic_faces"] == 122 and got["exposed_boundary_vertices"] == 122),
        ("26 value leaves", len(got["compact_value_certified_leaf_ids"]) == 26),
        ("ten stationary rejections", len(got["whole_line_stationary_rejected_leaf_ids"]) == 10),
        ("42 stationary retained", len(got["whole_line_stationary_retained_leaf_ids"]) == 42),
        ("no invented boundary closure", got["certified_exposed_atomic_faces"] == 0 and got["certified_exposed_boundary_vertices"] == 0),
        ("boundary open", not data["decision"]["all_slab_three_faces_and_vertices_certified"]),
        ("global withheld", not data["decision"]["global_optimizer_proved"]),
    ]


def main():
    got = compute()
    if not ARTIFACT.exists() or "--print" in __import__("sys").argv:
        print(json.dumps(got, indent=2)); return
    checks = validate(json.loads(ARTIFACT.read_text()), got)
    for i, (label, ok) in enumerate(checks, 1):
        assert ok, label
        print(f"PASS {i:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__":
    main()
