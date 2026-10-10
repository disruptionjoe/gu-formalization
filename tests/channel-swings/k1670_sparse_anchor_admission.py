#!/usr/bin/env python3
"""Certificate for K1670's protected integration."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def main():
    data = json.loads((ROOT / "lab/process/k1670-sparse-anchor-admission.json").read_text())
    claim, decision = data["admission"], data["decision"]
    checks = [
        ("schema", data["schema_version"] == "1.0"),
        ("claim", data["claim_id"] == "K1670"),
        ("subextensive result", "subextensive l2 mass" in claim["quantum_result"]),
        ("anchor result", "macroscopic positive anchor cube" in claim["quantum_result"]),
        ("positive gap", "positive Theta(N^4) gap" in claim["quantum_result"]),
        ("anchor-free wake", "anchor-free support geometry" in claim["remaining_quantum_gate"]),
        ("unknown wake", "unknown profiles" in claim["remaining_quantum_gate"]),
        ("physical gate", "K1145/K1150 remain 0/7" in claim["physical_admission"]),
        ("census", "385 rows" in claim["bridge_census"]),
        ("ledger", "33 SAME / 22 DIFFERS / 31 NEEDS / 2 OVER-DETERMINED" in claim["protected_state"]),
        ("scope", "Do not promote" in claim["scope_guard"]),
        ("sparse closed", decision["subextensive_profile_descent_closed"]),
        ("anchor closed", decision["anchored_degenerating_profile_class_closed"]),
        ("survivor open", decision["extensive_anchor_free_sector_open"]),
        ("source unchanged", not decision["source_status_changed"]),
        ("ledger unchanged", not decision["physics_ledger_changed"]),
        ("public unchanged", not decision["canon_or_public_status_changed"]),
    ]
    for number, (label, ok) in enumerate(checks, 1):
        assert ok, label
        print(f"PASS {number:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__": main()
