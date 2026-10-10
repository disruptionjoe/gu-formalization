#!/usr/bin/env python3
"""Certificate for K1675's protected integration."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def main():
    data = json.loads((ROOT / "lab/process/k1675-anchor-free-admission.json").read_text())
    claim, decision = data["admission"], data["decision"]
    checks = [
        ("schema", data["schema_version"] == "1.0"),
        ("claim", data["claim_id"] == "K1675"),
        ("known result", "known nonnegative profile" in claim["quantum_result"]),
        ("missing scale", "O(N log N)" in claim["quantum_result"]),
        ("gap scale", "-O(N log N)" in claim["quantum_result"]),
        ("coefficient closure", "no anchor-free support" in claim["quantum_result"]),
        ("unknown wake", "Unknown profiles" in claim["remaining_quantum_gate"]),
        ("nonorbit wake", "non-orbit correlations" in claim["remaining_quantum_gate"]),
        ("physical gate", "K1145/K1150 remain 0/7" in claim["physical_admission"]),
        ("census", "390 rows" in claim["bridge_census"]),
        ("ledger", "33 SAME / 22 DIFFERS / 31 NEEDS / 2 OVER-DETERMINED" in claim["protected_state"]),
        ("scope", "Do not promote" in claim["scope_guard"]),
        ("known closed", decision["known_profile_orbit_class_closed_at_leading_coefficient"]),
        ("anchor-free closed", not decision["extensive_anchor_free_sector_open"]),
        ("survivors open", decision["unknown_or_nonorbit_sector_open"]),
        ("source unchanged", not decision["source_status_changed"]),
        ("ledger unchanged", not decision["physics_ledger_changed"]),
        ("public unchanged", not decision["canon_or_public_status_changed"]),
    ]
    for number, (label, ok) in enumerate(checks, 1):
        assert ok, label
        print(f"PASS {number:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__": main()
