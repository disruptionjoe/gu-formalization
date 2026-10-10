#!/usr/bin/env python3
"""Certificate for K1680's protected integration."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def main():
    data = json.loads((ROOT / "lab/process/k1680-nonorbit-descent-admission.json").read_text())
    claim, decision = data["admission"], data["decision"]
    checks = [
        ("schema", data["schema_version"] == "1.0"), ("claim", data["claim_id"] == "K1680"),
        ("stationary", "stationary" in claim["quantum_result"]),
        ("nonorbit", "non-orbit" in claim["quantum_result"]),
        ("leading descent", "c_g N^4 below" in claim["quantum_result"]),
        ("lower-bound wake", "matching unrestricted lower bound" in claim["remaining_quantum_gate"]),
        ("profile wake", "unknown-profile" in claim["remaining_quantum_gate"]),
        ("physical gate", "K1145/K1150 remain 0/7" in claim["physical_admission"]),
        ("census total", "395 rows" in claim["bridge_census"]),
        ("census satisfied", "316 satisfied" in claim["bridge_census"]),
        ("source state", "SC-ACT-01/02/06 remain ASSERTS" in claim["protected_state"]),
        ("ledger state", "33 SAME / 22 DIFFERS / 31 NEEDS / 2 OVER-DETERMINED" in claim["protected_state"]),
        ("scope", "Do not promote" in claim["scope_guard"]),
        ("minimality false", decision["profiled_gaussian_unrestricted_leading_minimality_closed_false"]),
        ("true coefficient open", decision["true_unrestricted_coefficient_open"]),
        ("source unchanged", not decision["source_status_changed"]),
        ("ledger unchanged", not decision["physics_ledger_changed"]),
        ("public unchanged", not decision["canon_or_public_status_changed"]),
    ]
    for number, (label, ok) in enumerate(checks, 1):
        assert ok, label
        print(f"PASS {number:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__": main()
