#!/usr/bin/env python3
"""Replay the K1790 full-Fisher stationary admission boundary."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ARTIFACT = ROOT / "lab/process/k1790-full-fisher-stationary-admission.json"


def validate(data):
    census = data["bridge_census"]
    entry = data["entry_state"]
    decision = data["decision"]
    protected = data["protected_state"]
    checks = [
        ("schema", data["schema_version"] == "1.0"),
        ("claim", data["claim_id"] == "K1790"),
        ("inputs", data["inputs"] == ["K1785", "K1786", "K1787", "K1788", "K1789"]),
        ("census arithmetic", census["total"] == census["satisfied"] + census["conditional"] + census["excluded"] + census["missing"]),
        ("whole-line local jet", entry["whole_line_local_parameter_jet_available"]),
        ("slab three local point", entry["slab_three_unique_local_stationary_point"]),
        ("slab one boundary point", entry["slab_one_unique_local_boundary_kkt_point"]),
        ("slab two boundary point", entry["slab_two_unique_local_boundary_kkt_point"]),
        ("local order", entry["three_local_candidates_strictly_ordered"]),
        ("cover open", not entry["complete_complement_cover_available"]),
        ("slabs open", not decision["slabs_one_and_two_globally_excluded"]),
        ("slab three global open", not decision["unique_stationary_point_on_complete_slab_three"]),
        ("global open", not decision["global_optimizer_proved"]),
        ("physical open", not decision["source_owned_physical_theory"]),
        ("protected", not any(value for key, value in protected.items() if key.endswith("_changed"))),
        ("K1145", protected["k1145_score"] == "0/7"),
        ("K1150", protected["k1150_score"] == "0/7"),
    ]
    return checks


def main():
    data = json.loads(ARTIFACT.read_text())
    checks = validate(data)
    for i, (label, ok) in enumerate(checks, 1):
        assert ok, label
        print(f"PASS {i:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__":
    main()
