#!/usr/bin/env python3
"""Certificate for K1690's protected scalar-channel integration."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def main():
    data = json.loads((ROOT / "lab/process/k1690-scalar-channel-enlargement-admission.json").read_text())
    claim, decision = data["admission"], data["decision"]
    checks = [
        ("schema", data["schema_version"] == "1.0"),
        ("claim", data["claim_id"] == "K1690"),
        ("three-point result", "three-point seed locally beats Rademacher" in claim["quantum_result"]),
        ("heterogeneity result", "reduces exactly to one scalar-seed infimum" in claim["quantum_result"]),
        ("finite-t wake", "exact finite-t scalar infimum" in claim["remaining_quantum_gate"]),
        ("nonproduct wake", "non-product cumulant tensor" in claim["remaining_quantum_gate"]),
        ("Haar wake", "translation-Haar Fisher savings" in claim["remaining_quantum_gate"]),
        ("lower wake", "unrestricted lower bound" in claim["remaining_quantum_gate"]),
        ("physical gate", "K1145/K1150 remain 0/7" in claim["physical_admission"]),
        ("census total", "405 rows" in claim["bridge_census"]),
        ("census satisfied", "326 satisfied" in claim["bridge_census"]),
        ("source state", "SC-ACT-01/02/06 remain ASSERTS" in claim["protected_state"]),
        ("ledger state", "33 SAME / 22 DIFFERS / 31 NEEDS / 2 OVER-DETERMINED" in claim["protected_state"]),
        ("scope", "Do not promote" in claim["scope_guard"]),
        ("integrated", decision["scalar_channel_enlargement_integrated"]),
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
