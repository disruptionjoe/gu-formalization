#!/usr/bin/env python3
"""Compose the three certified local full-Fisher candidate values for K1789."""
import json
from pathlib import Path

from flint import arb

ROOT = Path(__file__).resolve().parents[2]
ARTIFACT = ROOT / "lab/process/k1789-full-fisher-global-comparison.json"
K1787 = ROOT / "lab/process/k1787-full-fisher-stationary-krawczyk.json"
K1788 = ROOT / "lab/process/k1788-full-fisher-first-two-slab-exclusion.json"


def compute():
    interior = json.loads(K1787.read_text())["certificate"]["stationary_value_enclosure"]
    boundaries = json.loads(K1788.read_text())["certificate"]["boundary_boxes"]
    v3 = arb(interior)
    rows = []
    for row in boundaries:
        value = arb(row["boundary_stationary_value_enclosure"])
        gap = arb(value.lower()) - arb(v3.upper())
        rows.append({
            "slab": row["slab"],
            "candidate_value": row["boundary_stationary_value_enclosure"],
            "lower_gap_above_slab_three_local_point": gap.str(38, radius=True, more=True),
            "strictly_above": bool(gap > 0),
        })
    return {"slab_three_candidate_value": interior, "comparisons": rows}


def validate(data, got=None):
    got = compute() if got is None else got
    cert = data["certificate"]
    checks = [
        ("schema", data["schema_version"] == "1.0"),
        ("claim", data["claim_id"] == "K1789"),
        ("slab three", arb(cert["slab_three_candidate_value"]).contains(
            arb(got["slab_three_candidate_value"]))),
        ("two comparisons", len(cert["comparisons"]) == len(got["comparisons"]) == 2),
    ]
    for old, new in zip(cert["comparisons"], got["comparisons"]):
        checks += [
            (f"slab {new['slab']} identity", old["slab"] == new["slab"]),
            (f"slab {new['slab']} positive gap", arb(old["lower_gap_above_slab_three_local_point"]) > 0),
            (f"slab {new['slab']} replay", arb(old["lower_gap_above_slab_three_local_point"]).contains(
                arb(new["lower_gap_above_slab_three_local_point"]))),
        ]
    checks += [
        ("local order", data["decision"]["three_local_candidates_strictly_ordered"]),
        ("not global", not data["decision"]["global_optimizer_proved"]),
    ]
    return checks


def main():
    if not ARTIFACT.exists() or "--print" in __import__("sys").argv:
        print(json.dumps(compute(), indent=2))
        return
    data = json.loads(ARTIFACT.read_text())
    checks = validate(data)
    for i, (label, ok) in enumerate(checks, 1):
        assert ok, label
        print(f"PASS {i:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__":
    main()
