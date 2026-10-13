#!/usr/bin/env python3
"""Replay K1791's exact degree-nine cover of the 59 interior tail cells."""
from hashlib import sha256
import importlib.util
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
ARTIFACT = ROOT / "lab/process/k1791-full-fisher-three-slab-tail-cover.json"
K1768_SOURCE = ROOT / "tests/channel-swings/k1768_bernstein_sublevel_partition.py"
K1771 = ROOT / "lab/process/k1771-interior-survivor-topology.json"
DEGREE = 9
MAX_DEPTH = 4


def load_k1768():
    spec = importlib.util.spec_from_file_location("k1768_for_k1791", K1768_SOURCE)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def enc(value):
    return str(value)


def replay():
    k1768 = load_k1768()
    topology = json.loads(K1771.read_text())["topology"]
    _, _, _, terms = k1768.threshold_polynomial(DEGREE)
    roots = []
    for slab_number, slab in enumerate(topology["slabs"], 1):
        ta, tb = map(k1768.Q, slab["t"])
        za, zb = map(k1768.Q, slab["z"])
        count = slab["cell_count"]
        for cell in range(count):
            z0 = za + (zb - za) * k1768.Q(cell, count)
            z1 = za + (zb - za) * k1768.Q(cell + 1, count)
            roots.append((slab_number, cell + 1, (ta, tb, z0, z1)))

    pruned = []
    retained = []
    stack = [(slab, cell, box, 0) for slab, cell, box in roots]
    while stack:
        slab, cell, box, depth = stack.pop()
        ta, tb, za, zb = box
        lower, upper = k1768.bernstein_bound(terms, (ta, tb), (za, zb))
        if lower > 0:
            pruned.append((slab, cell, box, depth))
            continue
        if depth == MAX_DEPTH:
            retained.append((slab, cell, box, depth))
            continue
        if depth % 2 == 0:
            middle = (ta + tb) / 2
            children = ((ta, middle, za, zb), (middle, tb, za, zb))
        else:
            middle = (za + zb) / 2
            children = ((ta, tb, za, middle), (ta, tb, middle, zb))
        stack.extend((slab, cell, child, depth + 1) for child in reversed(children))

    rows = []
    for kind, collection in (("P", pruned), ("R", retained)):
        for slab, cell, box, depth in collection:
            rows.append(f"{kind}:{slab}:{cell}:{depth}:" + ":".join(map(enc, box)))
    input_area = sum((box[1] - box[0]) * (box[3] - box[2]) for _, _, box in roots)
    retained_area = sum((box[1] - box[0]) * (box[3] - box[2]) for _, _, box, _ in retained)
    by_slab = []
    for slab in range(1, 4):
        slab_retained = [row for row in retained if row[0] == slab]
        hull = None
        if slab_retained:
            hull = {
                "t": [
                    enc(min(row[2][0] for row in slab_retained)),
                    enc(max(row[2][1] for row in slab_retained)),
                ],
                "z": [
                    enc(min(row[2][2] for row in slab_retained)),
                    enc(max(row[2][3] for row in slab_retained)),
                ],
            }
        by_slab.append({
            "slab": slab,
            "pruned_leaves": sum(row[0] == slab for row in pruned),
            "retained_leaves": len(slab_retained),
            "retained_input_cells": sorted({row[1] for row in slab_retained}),
            "retained_hull": hull,
        })
    return {
        "degree": DEGREE,
        "threshold": enc(k1768.UPPER),
        "input_topology_digest": topology["topology_digest"],
        "input_interior_cells": len(roots),
        "polynomial_terms": len(terms),
        "adaptive_split_order": ["t", "z", "t", "z"],
        "max_depth": MAX_DEPTH,
        "pruned_leaves": len(pruned),
        "retained_leaves": len(retained),
        "terminal_leaves": len(pruned) + len(retained),
        "unresolved_leaves": 0,
        "retained_fraction_of_input_area": enc(retained_area / input_area),
        "excluded_fraction_of_input_area": enc(1 - retained_area / input_area),
        "by_slab": by_slab,
        "partition_digest": sha256("\n".join(rows).encode()).hexdigest(),
    }


def validate(data, got=None):
    got = replay() if got is None else got
    decision = data["decision"]
    return [
        ("schema", data["schema_version"] == "1.0"),
        ("claim", data["claim_id"] == "K1791"),
        ("exact replay", data["partition"] == got),
        ("degree nine", got["degree"] == 9),
        ("59 input cells", got["input_interior_cells"] == 59),
        ("complete terminal partition", got["terminal_leaves"] == got["pruned_leaves"] + got["retained_leaves"]),
        ("zero unresolved", got["unresolved_leaves"] == 0),
        ("positive exact pruning", got["pruned_leaves"] > 0),
        ("strict area contraction", got["excluded_fraction_of_input_area"] != "0"),
        ("retained frontier nonempty", got["retained_leaves"] > 0),
        ("cover emitted", decision["complete_adaptive_partition_emitted"]),
        ("pruning certified", decision["every_pruned_leaf_has_positive_bernstein_lower_bound"]),
        ("retention is not membership", not decision["retained_leaf_means_below_threshold"]),
        ("not full-Fisher exclusion", not decision["complete_full_fisher_complement_excluded"]),
        ("not global", not decision["global_optimizer_proved"]),
    ]


def main():
    got = replay()
    if not ARTIFACT.exists() or "--print" in sys.argv:
        print(json.dumps(got, indent=2))
        return
    data = json.loads(ARTIFACT.read_text())
    checks = validate(data, got)
    for index, (label, ok) in enumerate(checks, 1):
        assert ok, label
        print(f"PASS {index:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__":
    main()
