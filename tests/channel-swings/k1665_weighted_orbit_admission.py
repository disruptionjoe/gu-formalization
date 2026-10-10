#!/usr/bin/env python3
"""Certificate for K1665's protected integration."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def main():
    data = json.loads((ROOT / "lab/process/k1665-weighted-orbit-admission.json").read_text())
    claim, decision = data["admission"], data["decision"]
    checks = [
        ("schema", data["schema_version"] == "1.0"),
        ("claim", data["claim_id"] == "K1665"),
        ("bounded profile result", "bounded positive amplitude profile" in claim["quantum_result"]),
        ("positive gap", "positive Theta(N^4)" in claim["quantum_result"]),
        ("sparse wake", "sparse or degenerating profile" in claim["remaining_quantum_gate"]),
        ("nonorbit wake", "non-orbit" in claim["remaining_quantum_gate"]),
        ("physical gate", "K1145/K1150 remain 0/7" in claim["physical_admission"]),
        ("census", "380 rows" in claim["bridge_census"]),
        ("ledger", "33 SAME / 22 DIFFERS / 31 NEEDS / 2 OVER-DETERMINED" in claim["protected_state"]),
        ("scope", "Do not promote" in claim["scope_guard"]),
        ("class closed", decision["bounded_profile_orbit_class_closed"]),
        ("sectors open", decision["degenerating_and_nonorbit_sectors_open"]),
        ("source unchanged", not decision["source_status_changed"]),
        ("ledger unchanged", not decision["physics_ledger_changed"]),
        ("public unchanged", not decision["canon_or_public_status_changed"]),
    ]
    for number, (label, ok) in enumerate(checks, 1):
        assert ok, label
        print(f"PASS {number:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__":
    main()
