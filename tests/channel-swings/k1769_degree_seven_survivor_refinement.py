#!/usr/bin/env python3
"""Exact degree-seven refinement of K1768's retained Hermite cells."""
import importlib.util
import json
from hashlib import sha256
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ARTIFACT = ROOT / "lab/process/k1769-degree-seven-survivor-refinement.json"
SOURCE = ROOT / "tests/channel-swings/k1768_bernstein_sublevel_partition.py"
spec = importlib.util.spec_from_file_location("k1768", SOURCE)
k1768 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(k1768)


def replay():
    degree_five = k1768.replay()
    value, numerator, denominator, terms = k1768.threshold_polynomial(7)
    pruned = []
    retained = []
    for box, _ in degree_five["retained"]:
        ta, tb, za, zb, _, _ = box
        tm, zm = (ta + tb) / 2, (za + zb) / 2
        center = k1768.horner_bound(terms, (tm, tm), (zm, zm))[0]
        if center > 0:
            bound = k1768.bernstein_bound(terms, (ta, tb), (za, zb))
            if bound[0] > 0:
                pruned.append((box, bound[0]))
                continue
        retained.append((box, (center, center)))
    rows = []
    for kind, collection in (("P", pruned), ("R", retained)):
        for item in collection:
            rows.append(kind + ":" + ":".join(k1768.encode_fraction(x) for x in item[0][:4]))
    digest = sha256("\n".join(rows).encode()).hexdigest()
    hull = None
    if retained:
        hull = (
            min(row[0][0] for row in retained),
            max(row[0][1] for row in retained),
            min(row[0][2] for row in retained),
            max(row[0][3] for row in retained),
        )
    return {
        "projection": value,
        "numerator": numerator,
        "denominator": denominator,
        "terms": terms,
        "input_partition_digest": degree_five["digest"],
        "input_retained": len(degree_five["retained"]),
        "pruned": pruned,
        "retained": retained,
        "digest": digest,
        "hull": hull,
    }


def summary(result):
    boundary = [row for row in result["retained"] if row[0][0] == k1768.T_BOX[0]]
    interior = [row for row in result["retained"] if row[0][0] != k1768.T_BOX[0]]
    def hull(rows):
        if not rows:
            return None
        values = (
            min(row[0][0] for row in rows), max(row[0][1] for row in rows),
            min(row[0][2] for row in rows), max(row[0][3] for row in rows),
        )
        return [k1768.encode_fraction(x) for x in values]
    return {
        "degree": 7,
        "threshold": k1768.encode_fraction(k1768.UPPER),
        "input_partition_digest": result["input_partition_digest"],
        "input_retained_leaves": result["input_retained"],
        "newly_pruned_leaves": len(result["pruned"]),
        "retained_leaves": len(result["retained"]),
        "unresolved_leaves": 0,
        "polynomial_terms": len(result["terms"]),
        "refinement_digest": result["digest"],
        "retained_hull": None if result["hull"] is None else [k1768.encode_fraction(x) for x in result["hull"]],
        "boundary_strip_leaves": len(boundary),
        "boundary_strip_hull": hull(boundary),
        "interior_retained_leaves": len(interior),
        "interior_retained_hull": hull(interior),
    }


def main():
    got = summary(replay())
    if not ARTIFACT.exists() or "--print" in __import__("sys").argv:
        print(json.dumps(got, indent=2))
        return
    data = json.loads(ARTIFACT.read_text())
    checks = [
        ("schema", data["schema_version"] == "1.0"),
        ("claim", data["claim_id"] == "K1769"),
        ("refinement replay", data["refinement"] == got),
        ("zero unresolved", got["unresolved_leaves"] == 0),
        ("accounting", got["newly_pruned_leaves"] + got["retained_leaves"] == got["input_retained_leaves"]),
        ("not full Fisher", not data["decision"]["full_fisher_interval_newton_completed"]),
        ("not optimizer", not data["decision"]["global_optimizer_proved"]),
    ]
    for index, (label, ok) in enumerate(checks, 1):
        assert ok, label
        print(f"PASS {index:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__":
    main()
