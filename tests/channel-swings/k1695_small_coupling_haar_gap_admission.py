#!/usr/bin/env python3
"""Certificate for K1695's protected integration."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def main():
    data = json.loads((ROOT / "lab/process/k1695-small-coupling-haar-gap-admission.json").read_text())
    claim, decision = data["admission"], data["decision"]
    checks = [
        ("schema", data["schema_version"] == "1.0"),
        ("claim", data["claim_id"] == "K1695"),
        ("optimized fixed shape", "globally optimized three-point scalar branch" in claim["quantum_result"]),
        ("explicit cubic", "explicit positive cubic term" in claim["quantum_result"]),
        ("strict Haar", "strict exact finite-cutoff Fisher saving" in claim["quantum_result"]),
        ("uniform shape wake", "uniform shape control" in claim["remaining_quantum_gate"]),
        ("finite strength wake", "finite-strength scalar infimum" in claim["remaining_quantum_gate"]),
        ("Haar scale wake", "asymptotic order of Haar saving" in claim["remaining_quantum_gate"]),
        ("lower wake", "unrestricted lower bound" in claim["remaining_quantum_gate"]),
        ("physical gate", "K1145/K1150 remain 0/7" in claim["physical_admission"]),
        ("census total", "410 rows" in claim["bridge_census"]),
        ("census satisfied", "331 satisfied" in claim["bridge_census"]),
        ("source state", "SC-ACT-01/02/06 remain ASSERTS" in claim["protected_state"]),
        ("ledger state", "33 SAME / 22 DIFFERS / 31 NEEDS / 2 OVER-DETERMINED" in claim["protected_state"]),
        ("scope", "Do not promote" in claim["scope_guard"]),
        ("integrated", decision["small_coupling_and_haar_gap_integrated"]),
        ("coefficient open", decision["true_unrestricted_coefficient_open"]),
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
